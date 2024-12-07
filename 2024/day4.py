#!/usr/bin/env python
import re
from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input04.txt"

PUZZLE_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
SEARCH_WORD = "XMAS"

#TODO Part 2

def parse_input(lines, letter):
    lines_to_letter = defaultdict(list)
    for line_number, line in enumerate(lines):
        for match in re.finditer(letter, line):
            lines_to_letter[line_number].append(int(match.start()))
    return lines_to_letter


def is_word_around(lines, start_position, delta_x, delta_y, search_word):
    row, column = start_position
    for letter in search_word:
        try:
            if row < 0 or column < 0 or lines[row][column] != letter:
                return False
            row += delta_x
            column += delta_y
        except IndexError:
            return False
    return True


def count_words(lines, lines_to_letter, search_word, delta):
    words_counter = []
    for row, columns in lines_to_letter.items():
        for column in columns:
            words_counter.extend(
                is_word_around(lines, (row, column), delta_x, delta_y, search_word)
                for delta_x, delta_y in delta
            )
    return sum(words_counter)


def main():
    puzzle_input = PUZZLE_INPUT
    # puzzle_input = INPUT_FILE.read_text(encoding="UTF-8").splitlines()
    lines_to_x = parse_input(puzzle_input, "X")
    print(count_words(puzzle_input, lines_to_x, SEARCH_WORD, DELTA))



if __name__ == "__main__":
    main()
