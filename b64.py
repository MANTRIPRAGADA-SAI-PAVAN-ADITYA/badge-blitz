import sys
import base64


def encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def decode(text: str) -> str:
    return base64.b64decode(text.encode()).decode()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python b64.py encode <text>  |  python b64.py decode <text>")
        sys.exit(1)
    mode, value = sys.argv[1], " ".join(sys.argv[2:])
    print(encode(value) if mode == "encode" else decode(value))
