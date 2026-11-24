"""Write the robot vacuum's best excuse for missing a spot.

This tiny program writes a single one-line excuse, spoken by a robot
vacuum to its tired homeowner, to the output file. The line is at most
140 characters long, contains no newline, and is written with no
trailing newline so the file holds exactly one line.
"""

import os
import sys

LINE = "I didn't miss that spot \u2014 my map filed it under 'haunted' and I don't do ghosts."


def output_path():
    """Return the output path, honouring MAKEFUN_OUTPUT_DIR when set."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory and directory.strip():
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    """Validate the line, write it, verify it, and print it."""
    if not LINE or not LINE.strip():
        print("error: line is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(LINE) > 140:
        print(f"error: line is {len(LINE)} characters, exceeds 140", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line contains a newline", file=sys.stderr)
        return 1

    path = output_path()
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(LINE)
        with open(path, "rb") as handle:
            written = handle.read()
        if written != LINE.encode("utf-8"):
            print("error: written content does not match the line", file=sys.stderr)
            return 1
    except OSError as exc:
        print(f"error: failed to write output: {exc}", file=sys.stderr)
        return 1

    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
