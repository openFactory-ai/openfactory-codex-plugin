"""Build a fresh portable release ZIP using only the Python standard library."""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parents[1]
plugin = root / "plugins" / "openfactory"
manifest = json.loads((plugin / "plugin.json").read_text())
output = root / "dist" / f"openfactory-{manifest['version']}.zip"
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
    for path in sorted(plugin.rglob("*")):
        if path.is_file():
            archive.write(path, path.relative_to(plugin))
print(output)
