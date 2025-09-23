#!/usr/bin/env python3

from itertools import product
from operator import add, mul as multiply

from tqdm import tqdm

from pathlib import Path
from pprint import pprint

INPUT_FILE = Path(__file__).parent / "input07.txt"

PUZZLE_INPUT = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".splitlines()


def concatenate(a, b):
    return int(f"{a}{b}")


def check_calibration(result, operands, base_operations):
    for operations in product(base_operations, repeat=len(operands) - 1):
        operands_iterator = iter(operands)
        value = next(operands_iterator)
        for operation, operand in zip(operations, operands_iterator):
            value = operation(value, operand)

        if value == result:
            return True

    return False


def parse_input(lines):
    return [
        (int(result), list(map(int, values.split())))
        for (result, values) in map(lambda x: x.split(":"), lines)
    ]


def sum_solvable_calibrations(calibrations, operations):
    return sum(
        result
        for result, operands in calibrations
        if check_calibration(result, operands, operations)
    )


def main():
    calibrations = parse_input(INPUT_FILE.read_text(encoding="UTF-8").splitlines())
    # calibrations = parse_input(PUZZLE_INPUT)
    print(sum_solvable_calibrations(calibrations, [multiply, add]))
    print(sum_solvable_calibrations(tqdm(calibrations), [multiply, concatenate, add]))


if __name__ == "__main__":
    main()
