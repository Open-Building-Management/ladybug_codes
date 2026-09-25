"""merge epw files"""
from pathlib import Path
import sys


def merge_epw(directory, output, start_year=2025):
    """merge all epw files in a directory
    adjust years"""
    files = sorted(Path(directory).glob("*.epw"))

    if not files:
        raise ValueError(f"No EPW files found in {directory}")

    total_hours = 0

    with open(output, "w", encoding="utf-8") as out:
        for i, filename in enumerate(files):
            with open(filename, encoding="utf-8") as f:
                lines = f.readlines()

            data = lines[8:]

            if i == 0:
                out.writelines(lines[:8])

            year = start_year + i

            for line in data:
                fields = line.rstrip("\n").split(",")
                if len(fields) >= 35:
                    fields[0] = str(year)
                    out.write(",".join(fields) + "\n")

            total_hours += len(data)

    print(f"{len(files)} EPW files")
    print(f"{total_hours} hourly records")
    print(f"Expected: {len(files) * 8760}")
    print(f"Output: {output}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_epw.py <directory> <output.epw>")
        sys.exit(1)

    merge_epw(sys.argv[1], sys.argv[2])
