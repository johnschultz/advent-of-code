# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python, managed with `uv`.

## Structure

Each day's puzzle is located in its own directory (e.g., `day01`, `day02`).
Inside each directory:
- `solution.py`: The Python script containing the solution.
- `input.txt`: The puzzle input file.

## Usage

### Prerequisites
- [uv](https://github.com/astral-sh/uv) installed.

### Running a Solution

To run the solution for a specific day (e.g., Day 1), run the following command from the project root:

```bash
uv run day01/solution.py
```

## Setup for a New Day

1. Create a new directory `dayXX`.
2. Add your puzzle input to `dayXX/input.txt`.
3. Create a `solution.py` script.

## Notes

- The `input.txt` files are ignored by git (added to `.gitignore`) to respect Advent of Code copyright, but you should download them yourself from the official site.