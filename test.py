import os
import pathlib

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # pip install tomli

p = os.environ.get("SNOWFLAKE_CONNECTIONS")
if not p:
    p = str(pathlib.Path.home() / ".snowflake" / "connections.toml")

path = pathlib.Path(p)
print("Using file:", path)
data = tomllib.loads(path.read_bytes())

print("Top-level keys:", list(data.keys()))
print("connections keys:", list(data.get("connections", {}).keys()))
