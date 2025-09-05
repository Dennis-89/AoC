#!/usr/bin/env python
from itertools import pairwise
from pathlib import Path


INPUT_FILE = Path(__file__).parent / "input02.txt"
PUZZLE_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".splitlines()


def is_safe(report):
    return all(1 <= x - y <= 3 for x, y in pairwise(report)) or all(
        1 <= y - x <= 3 for x, y in pairwise(report)
    )


def get_safe_reports(reports):
    return sum(map(is_safe, reports))


def skip_index(iterable, index):
    for i, value in enumerate(iterable):
        if i != index:
            yield value


def get_tolerated_safe_reports(reports):
    safe_reports = 0
    for report in reports:
        if not (safe := is_safe(report)):
            for changed_report in map(lambda i: skip_index(report, i), range(len(report))):
                if safe := is_safe(list(changed_report)):
                    break
        safe_reports += safe
    return safe_reports


def main():
    puzzle_input = PUZZLE_INPUT
    puzzle_input = INPUT_FILE.read_text(encoding="UTF-8").splitlines()
    reports = list(map(lambda x: list(map(int, x.split())), puzzle_input))
    print(get_safe_reports(reports))
    print(get_tolerated_safe_reports(reports))


if __name__ == "__main__":
    main()
