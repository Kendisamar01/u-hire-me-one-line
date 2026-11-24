from pathlib import Path
import sys

SOURCE = Path(__file__).resolve().parent / "entry.txt"
TARGET = Path("/output/entry.txt")


def main():
    try:
        entry = SOURCE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        print(f"Error: entry.txt not found at {SOURCE}", file=sys.stderr)
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(entry, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
