import sys
import re


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    r, g, b = r / 255, g / 255, b / 255
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    l = (cmax + cmin) / 2
    s = 0 if delta == 0 else delta / (1 - abs(2 * l - 1))
    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)
    return round(h, 1), round(s * 100, 1), round(l * 100, 1)


def convert(hex_color: str) -> None:
    if not re.match(r"^#?[0-9a-fA-F]{6}$", hex_color):
        print("Invalid hex color. Example: #ff6b6b")
        return
    r, g, b = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(r, g, b)
    print(f"  HEX  {hex_color.upper()}")
    print(f"  RGB  rgb({r}, {g}, {b})")
    print(f"  HSL  hsl({h}, {s}%, {l}%)")


if __name__ == "__main__":
    color = sys.argv[1] if len(sys.argv) > 1 else "#3498db"
    convert(color)
