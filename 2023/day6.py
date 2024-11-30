#!/usr/bin/env python3
from pathlib import Path


INPUT = Path("/home/dennis/AoC/2023/Day6/input.txt")

EXAMPLE_LINES = """\
Time:      7  15   30
Distance:  9  40  200""".splitlines()


def parse_input(input_lines):
    return (list(map(int, line.split()[1:])) for line in input_lines)



def main():
    #cards = parse_cards(INPUT.read_text(encoding="UTF-8").splitlines())
    times, record = parse_input(EXAMPLE_LINES)




if __name__ == "__main__":
    main()