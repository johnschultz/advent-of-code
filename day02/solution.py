import re
from collections import namedtuple
from pathlib import Path
from typing import List

IDRange = namedtuple("IDRange", ["start", "end"], defaults=[0, 0])


def parse_ranges(input: str):
    for id_range in input.split(","):
        start, end = (int(x) for x in id_range.split("-"))
        yield from range(start, end + 1)


def part1(data: str) -> int:
    """Sum invalid ids, where an id is invalid if it contains a single sequence of digits repeated twice."""
    sum = 0
    for id in parse_ranges(data):
        sid = str(id)
        if sid[: len(sid) // 2] == sid[len(sid) // 2 :]:
            print(f"{sid} Match!")
            sum += id
        else:
            print(f"{sid}")
    return sum


def part2(data):
    """Sum invalid ids, where an id is invalid if it contains a single sequence of digits any number of times."""
    sum = 0
    regex = re.compile(r"(.+?)\1+")
    for id in parse_ranges(data):
        sid = str(id)
        if regex.fullmatch(sid):
            print(f"{sid} Match!")
            sum += id
        else:
            print(f"{sid}")
    return sum


def main():
    input_path = Path(__file__).parent / "input.txt"
    if not input_path.exists():
        print(f"Error: Input file not found at {input_path}")
        print(
            "Please download your input from https://adventofcode.com/2025/day/1/input"
        )
        return

    with open(input_path, "r") as f:
        data = f.read().strip()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
