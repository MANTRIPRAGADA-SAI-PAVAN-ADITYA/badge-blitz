import sys
import json
from pathlib import Path


def pretty(data: dict | list, indent: int = 2) -> str:
    return json.dumps(data, indent=indent, ensure_ascii=False)


def flatten(obj: dict, prefix: str = "", sep: str = ".") -> dict:
    out = {}
    for k, v in obj.items():
        key = f"{prefix}{sep}{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, key, sep))
        else:
            out[key] = v
    return out


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if path:
        text = Path(path).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    data = json.loads(text)
    if "--flatten" in sys.argv:
        print(pretty(flatten(data)))
    else:
        print(pretty(data))
