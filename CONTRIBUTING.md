# Contributing

## Plugin contract

- Plugin directories use kebab-case and live under `plugins/`.
- Every plugin must contain both `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`.
- The directory name, catalog entry name, and both manifest names must match.
- Both manifests must carry the same semantic version.
- Shared skills use `skills/<skill-name>/SKILL.md` with `name` and `description` frontmatter.
- Keep platform-specific metadata in its platform manifest. Keep workflow instructions in shared skills.
- Do not reference files outside a plugin directory; Claude copies installed plugins into a cache.
- Remote MCP servers belong in the plugin's `.mcp.json`. Never commit OAuth tokens, bearer tokens, or client secrets.
- Never embed private equity-research content, evidence IDs, licensed excerpts, or authenticated links in plugin source, fixtures, or examples.

## Release checklist

1. Update skills, references, and plugin documentation.
2. Bump the version in both platform manifests.
3. Run `npm run validate`.
4. If available, run `claude plugin validate .` and strict validation on each plugin.
5. Run `npm run package:cowork` and inspect the archive contents.
6. Test local installation in Codex and Claude Code.
7. Start a new session and exercise each changed skill.

Never publish secrets, customer data, data-room material, or proprietary evidence in a plugin or fixture.
