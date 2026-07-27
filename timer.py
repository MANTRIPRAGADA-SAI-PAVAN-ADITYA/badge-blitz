import time
import sys


def countdown(minutes: int) -> None:
    total = minutes * 60
    print(f"Timer started: {minutes} minute(s)")
    try:
        while total > 0:
            mins, secs = divmod(total, 60)
            print(f"\r  {mins:02d}:{secs:02d} remaining", end="", flush=True)
            time.sleep(1)
            total -= 1
        print("\r  00:00 — Time's up! \a")
    except KeyboardInterrupt:
        print("\n  Timer cancelled.")


if __name__ == "__main__":
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    countdown(minutes)
