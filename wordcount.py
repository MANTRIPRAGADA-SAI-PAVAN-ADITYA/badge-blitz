import sys


def analyze(text: str) -> dict:
    words = text.split()
    return {
        "chars": len(text),
        "words": len(words),
        "lines": text.count("\n") + 1,
        "unique": len(set(w.lower().strip(".,!?;:") for w in words)),
    }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    r = analyze(text)
    print(f"  Lines   {r['lines']}")
    print(f"  Words   {r['words']}")
    print(f"  Unique  {r['unique']}")
    print(f"  Chars   {r['chars']}")
