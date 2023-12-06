import contextlib
import re
from pathlib import Path


INPUT = Path("/home/dennis/AoC/2023/Day3/input.txt")

EXAMPLE_LINES = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()


def parse_input(lines):
    line_to_parts = {number: [] for number in range(len(lines))}
    line_to_symbols = {number: [] for number in range(len(lines))}
    for line_number, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            line_to_parts[line_number].append(
                {
                    "start": int(match.start()),
                    "end": int(match.end()),
                    "number": int(match.group(0)),
                }
            )
        for match in re.finditer(r"[^\d.\n]", line):
            line_to_symbols[line_number].append(int(match.start()))
    return line_to_parts, line_to_symbols


def looking_for_symbol(line_to_parts, line_to_symbols):
    found_parts = []
    for line, positions in line_to_parts.items():
        for position_details in positions:
            for x in range(position_details["start"] - 1, position_details["end"] + 1):
                for delta in [-1, 0, 1]:
                    with contextlib.suppress(KeyError):
                        if x in line_to_symbols[line + delta]:
                            found_parts.append(position_details["number"])
    return found_parts


# TODO Part 2 is missing
def main():
    engine_parts = list(INPUT.read_text(encoding="UTF-8").splitlines())
    # engine_parts = EXAMPLE_LINES
    line_to_parts, line_to_symbols = parse_input(engine_parts)
    print(sum(looking_for_symbol(line_to_parts, line_to_symbols)))


if __name__ == "__main__":
    main()
