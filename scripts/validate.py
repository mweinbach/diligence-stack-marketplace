#!/usr/bin/env python3
"""Validate the cross-platform marketplace without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CODEX_CATALOG = ROOT / ".agents" / "plugins" / "marketplace.json"
CLAUDE_CATALOG = ROOT / ".claude-plugin" / "marketplace.json"
EVAL_SCENARIOS = ROOT / "evals" / "scenarios.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_MCP_URL = "https://portal.thediligencestack.com/mcp"
BRAND_SKILL = "diligence-brand-guidelines"
BRAND_GUIDE_LINK = "(../diligence-brand-guidelines/SKILL.md)"
CANONICAL_PUBLIC_HOST = "www.thediligencestack.com"
PORTAL_HOST = "portal.thediligencestack.com"
WEB_URL = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
BRAND_ASSETS = {
    "creative-strategies-mark.png",
    "diligence-stack-logo.png",
    "diligence-stack-wordmark.jpeg",
}
BRAND_REQUIRED_MARKERS = {
    "#FF6719",
    "#FBBB14",
    "#363737",
    "Inter",
    "The Diligence Stack —",
    "Research and citations: The Diligence Stack by Creative Strategies.",
    "exact hostname is `www.thediligencestack.com`",
}


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return {}


def skill_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)} has no YAML frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path.relative_to(ROOT)} has unclosed YAML frontmatter")
        return {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def validate_user_facing_urls(skill_root: Path, errors: list[str]) -> None:
    for path in sorted(skill_root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in WEB_URL.finditer(text):
            url = match.group(0).rstrip(".,;:")
            parsed = urlsplit(url)
            if parsed.scheme != "https" or parsed.hostname != CANONICAL_PUBLIC_HOST:
                errors.append(
                    f"{path.relative_to(ROOT)} contains non-canonical user-facing URL {url!r}"
                )


def validate_no_portal_urls_in_markdown(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or "dist" in path.parts:
            continue
        if PORTAL_HOST in path.read_text(encoding="utf-8"):
            errors.append(f"{path.relative_to(ROOT)} exposes the private portal URL")


def main() -> int:
    errors: list[str] = []
    available_skills: set[str] = set()
    codex = load_json(CODEX_CATALOG, errors)
    claude = load_json(CLAUDE_CATALOG, errors)

    if codex.get("name") != claude.get("name"):
        errors.append("marketplace names differ between Codex and Claude catalogs")

    codex_entries = {entry.get("name"): entry for entry in codex.get("plugins", [])}
    claude_entries = {entry.get("name"): entry for entry in claude.get("plugins", [])}
    if set(codex_entries) != set(claude_entries):
        errors.append("Codex and Claude catalogs list different plugins")

    if None in codex_entries or None in claude_entries:
        errors.append("every catalog entry must have a name")

    for name in sorted(set(codex_entries) | set(claude_entries), key=lambda value: value or ""):
        if not name or not KEBAB.fullmatch(name):
            errors.append(f"invalid plugin name: {name!r}")
            continue

        plugin = ROOT / "plugins" / name
        codex_manifest = load_json(plugin / ".codex-plugin" / "plugin.json", errors)
        claude_manifest = load_json(plugin / ".claude-plugin" / "plugin.json", errors)

        for platform, manifest in (("Codex", codex_manifest), ("Claude", claude_manifest)):
            if manifest.get("name") != name:
                errors.append(f"{platform} manifest name does not match {name}")
            version = manifest.get("version", "")
            if not SEMVER.fullmatch(version):
                errors.append(f"{platform} manifest for {name} has invalid version {version!r}")

        if codex_manifest.get("version") != claude_manifest.get("version"):
            errors.append(f"manifest versions differ for {name}")

        for platform, manifest in (("Codex", codex_manifest), ("Claude", claude_manifest)):
            if manifest.get("mcpServers") != "./.mcp.json":
                errors.append(f"{platform} manifest for {name} must load ./.mcp.json")

        mcp = load_json(plugin / ".mcp.json", errors)
        server = mcp.get("mcpServers", {}).get("diligence-stack", {})
        if server.get("type") != "http" or server.get("url") != EXPECTED_MCP_URL:
            errors.append(f"{name} must configure the Diligence Stack HTTP MCP endpoint")
        forbidden_auth = {"headers", "env", "oauth", "bearer_token_env_var"} & set(server)
        if forbidden_auth:
            errors.append(
                f"{name} MCP config must use native OAuth discovery, not {sorted(forbidden_auth)}"
            )

        codex_path = codex_entries.get(name, {}).get("source", {}).get("path")
        claude_path = claude_entries.get(name, {}).get("source")
        expected = f"./plugins/{name}"
        if codex_path != expected:
            errors.append(f"Codex source for {name} must be {expected!r}")
        if claude_path != expected:
            errors.append(f"Claude source for {name} must be {expected!r}")

        skill_root = plugin / "skills"
        skills = sorted(skill_root.glob("*/SKILL.md"))
        if not skills:
            errors.append(f"{name} has no skills")
        seen_skills: set[str] = set()
        for skill in skills:
            fields = skill_frontmatter(skill, errors)
            skill_name = fields.get("name", "")
            if skill_name != skill.parent.name:
                errors.append(f"skill name in {skill.relative_to(ROOT)} must match its directory")
            if not fields.get("description"):
                errors.append(f"{skill.relative_to(ROOT)} has no description")
            if skill_name in seen_skills:
                errors.append(f"duplicate skill name {skill_name!r} in {name}")
            seen_skills.add(skill_name)
            available_skills.add(skill_name)

            skill_text = skill.read_text(encoding="utf-8")
            if "[TODO" in skill_text:
                errors.append(f"{skill.relative_to(ROOT)} contains a TODO placeholder")
            if skill_name != BRAND_SKILL and BRAND_GUIDE_LINK not in skill_text:
                errors.append(
                    f"{skill.relative_to(ROOT)} must load the Diligence Stack brand guidelines"
                )
            if skill_name == BRAND_SKILL:
                missing_markers = sorted(
                    marker for marker in BRAND_REQUIRED_MARKERS if marker not in skill_text
                )
                if missing_markers:
                    errors.append(
                        f"{skill.relative_to(ROOT)} is missing brand-policy markers: "
                        f"{missing_markers}"
                    )

            openai_yaml = skill.parent / "agents" / "openai.yaml"
            if not openai_yaml.exists():
                errors.append(f"{skill.parent.relative_to(ROOT)} has no agents/openai.yaml")
            else:
                metadata = openai_yaml.read_text(encoding="utf-8")
                if f"${skill_name}" not in metadata:
                    errors.append(
                        f"{openai_yaml.relative_to(ROOT)} default prompt must mention ${skill_name}"
                    )
                if EXPECTED_MCP_URL not in metadata or 'value: "diligence-stack"' not in metadata:
                    errors.append(
                        f"{openai_yaml.relative_to(ROOT)} must declare the Diligence Stack MCP dependency"
                    )

        brand_assets = skill_root / BRAND_SKILL / "assets"
        missing_brand_assets = sorted(
            asset for asset in BRAND_ASSETS if not (brand_assets / asset).is_file()
        )
        if missing_brand_assets:
            errors.append(f"{name} is missing brand assets: {missing_brand_assets}")
        validate_user_facing_urls(skill_root, errors)

    validate_no_portal_urls_in_markdown(errors)

    evals = load_json(EVAL_SCENARIOS, errors)
    scenarios = evals.get("scenarios", [])
    if evals.get("version") != 1 or not isinstance(scenarios, list) or not scenarios:
        errors.append("evals/scenarios.json must contain version 1 and a non-empty scenarios array")
    else:
        scenario_ids: set[str] = set()
        for index, scenario in enumerate(scenarios):
            scenario_id = scenario.get("id")
            if not scenario_id or scenario_id in scenario_ids:
                errors.append(f"eval scenario {index} has a missing or duplicate id")
            scenario_ids.add(scenario_id)
            if not scenario.get("prompt"):
                errors.append(f"eval scenario {scenario_id!r} has no prompt")
            expected = scenario.get("expected_skills", [])
            unknown = set(expected) - available_skills
            if not expected or unknown:
                errors.append(
                    f"eval scenario {scenario_id!r} has missing or unknown skills: {sorted(unknown)}"
                )
            if not scenario.get("success_criteria"):
                errors.append(f"eval scenario {scenario_id!r} has no success criteria")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(codex_entries)} plugin(s), {len(available_skills)} skills, "
        f"and {len(scenarios)} eval scenarios across Codex and Claude catalogs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
