#!/usr/bin/env python3
"""Create Claude Cowork-compatible plugin zip archives."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
DIST = ROOT / "dist"
IGNORED_PARTS = {".codex-plugin", "__pycache__"}


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    archives = 0
    for plugin in sorted(path for path in PLUGINS.iterdir() if path.is_dir()):
        manifest_path = plugin / ".claude-plugin" / "plugin.json"
        if not manifest_path.exists():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        version = manifest["version"]
        archive = DIST / f"{plugin.name}-{version}.zip"
        with ZipFile(archive, "w", ZIP_DEFLATED) as output:
            for path in sorted(plugin.rglob("*")):
                if not path.is_file() or any(part in IGNORED_PARTS for part in path.parts):
                    continue
                output.write(path, path.relative_to(plugin).as_posix())
        print(f"Created {archive.relative_to(ROOT)}")
        archives += 1

    if not archives:
        raise SystemExit("No Claude plugins found to package")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
