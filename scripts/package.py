"""Build a fresh portable release ZIP using only the Python standard library.

The OpenAI upload is an Agent Plugins 1.0.0 package: `packaging/openai/plugin.json`
and `mcp.json` become its root manifest. The repository's plugin directory carries the
native Codex manifest instead (`.codex-plugin/plugin.json`, `.mcp.json`), because Codex
caps an agent-schema plugin's MCP tools at 64 KB and hid most of OpenFactory's.
"""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parents[1]
plugin = root / "plugins" / "openfactory"
openai = root / "packaging" / "openai"
manifest = json.loads((openai / "plugin.json").read_text())
native_only = {Path(".codex-plugin"), Path(".mcp.json")}
output = root / "dist" / f"openfactory-{manifest['version']}.zip"
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
    for name in ("plugin.json", "mcp.json"):
        archive.write(openai / name, name)
    for path in sorted(plugin.rglob("*")):
        relative = path.relative_to(plugin)
        if path.is_file() and not native_only & {relative, *relative.parents}:
            archive.write(path, relative)
print(output)
