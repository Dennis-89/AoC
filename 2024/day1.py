#!/usr/bin/env python
from collections import Counter
from itertools import chain
from pathlib import Path

from more_itertools import distribute

INPUT_FILE = Path(__file__).parent / "input01.txt"
PUZZLE_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
""".splitlines()


def part_1(left_numbers, right_numbers):
    return sum(
        abs(left - right)
        for left, right in zip(*map(sorted, (left_numbers, right_numbers)))
    )


def part_2(left_numbers, right_numbers):
    number_of_destinations = Counter(right_numbers)
    return sum(left * number_of_destinations[left] for left in left_numbers)


def main():
    # puzzle_input = INPUT_FILE.read_text(encoding='UTF-8').splitlines()
    puzzle_input = PUZZLE_INPUT
    destinations = distribute(
        2, chain.from_iterable([map(int, line.split()) for line in puzzle_input])
    )
    left, right = map(list, destinations)
    print(part_1(left, right))
    print(part_2(left, right))


if __name__ == "__main__":
    main()
