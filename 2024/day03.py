#!/usr/bin/env python
import re
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input03.txt"

PUZZLE_INPUT = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".splitlines()


EXPRESSION = re.compile(r"mul\(\d*,\d*\)|don't\(\)|do\(\)")


def parse_input(lines):
    expressions = []
    for line in lines:
        expressions.extend(re.findall(EXPRESSION, line))
    return expressions


def decode_expression(expression):
    if expression.startswith("mul"):
        return map(int, re.findall(r"\d*,\d*", expression)[0].split(","))
    return 0, 0


def get_mul(mul):
    x, y = decode_expression(mul)
    return x * y


def run_mul_expressions(expressions):
    return sum(get_mul(expression) for expression in expressions)


def run_and_enable_mul_expressions(expressions):
    run = True
    multiples = []
    for expression in expressions:
        if expression == "don't()":
            run = False
        elif expression == "do()":
            run = True
        elif run:
            multiples.append(get_mul(expression))
    return sum(multiples)


def main():
    puzzle_input = PUZZLE_INPUT
    puzzle_input = INPUT_FILE.read_text(encoding="UTF-8").splitlines()
    expressions = parse_input(puzzle_input)
    print(run_mul_expressions(expressions))
    print(run_and_enable_mul_expressions(expressions))


if __name__ == "__main__":
    main()
