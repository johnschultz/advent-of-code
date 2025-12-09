from pathlib import Path
from typing import List


def parseRotation(rotation: str) -> int:
    direction = rotation[0]
    distance = int(rotation[1:])
    distance *= 1 if direction == "R" else -1
    return distance


def part1(data: List[str]) -> int:
    """Enter a combination to a safe and count the number of times the dial stops (not pass) on zero."""
    zero_count: int = 0
    dial_pos: int = 50
    DIAL_MAX: int = 100

    for rotation in data:
        distance = parseRotation(rotation)
        dial_pos = (dial_pos + distance) % DIAL_MAX
        if dial_pos == 0:
            zero_count += 1
    return zero_count


def part2(data):
    """Enter a combination to a safe and count the number of times the dial points at zero during or after a rotation."""
    zero_count: int = 0
    dial_pos: int = 50
    DIAL_MAX: int = 100

    for rotation in data:
        direction = 1 if rotation[0] == "R" else -1
        distance = int(rotation[1:])
        start_pos = dial_pos

        # count the number of full rotations
        zero_count += distance // DIAL_MAX
        distance %= DIAL_MAX

        dial_pos += direction * distance
        if start_pos == 0 and direction < 0:
            # if the start_pos is 0 and we're going lower, then we do nothing to avoid overcounting in the else clause
            pass
        elif dial_pos == 0:
            # if we land on 0 exactly, we need to add one rotation
            zero_count += 1
        else:
            # otherwise just count the number of full rotations (should ever be one)
            zero_count += abs(dial_pos // DIAL_MAX)

        dial_pos %= DIAL_MAX
    return zero_count


def main():
    input_path = Path(__file__).parent / "input.txt"
    if not input_path.exists():
        print(f"Error: Input file not found at {input_path}")
        print(
            "Please download your input from https://adventofcode.com/2025/day/1/input"
        )
        return

    with open(input_path, "r") as f:
        data = f.read().strip().split("\n")

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
