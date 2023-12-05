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
            line_to_parts[line_number].append(match.span())
        for match in re.finditer(r"[^\d.\n]", line):
            line_to_symbols[line_number].append(match.span()[0])
    return line_to_parts, line_to_symbols

# TODO in Process
def main():
    engine_parts = list(INPUT.read_text(encoding="UTF-8").splitlines())
    line_to_parts, line_to_symbols = parse_input(engine_parts)
    found_parts = []
    print(line_to_parts)
    print(line_to_symbols)
    for line, position in line_to_symbols.items():
        if position - 1 in line_to_parts[line]:
            found_parts.append(engine_parts[line])



if __name__ == "__main__":
    main()
