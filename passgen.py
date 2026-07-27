import secrets
import string
import sys


def generate(length: int = 16, symbols: bool = True) -> str:
    pool = string.ascii_letters + string.digits
    if symbols:
        pool += "!@#$%^&*"
    return "".join(secrets.choice(pool) for _ in range(length))


if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    no_symbols = "--no-symbols" in sys.argv
    print(generate(length, symbols=not no_symbols))
