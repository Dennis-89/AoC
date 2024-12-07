#!/usr/bin/env python
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "input06.txt"

PUZZLE_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

def get_start_position(guard_map):
    for row, places in enumerate(guard_map):
        column = places.find("^")
        if column != -1:
            return row, column


def count_visited_places(start_position, guard_map):
    visit_places = 1
    y, x = start_position
    already_visited = [(y, x)]
    while True:
        for (delta_y, delta_x) in DIRECTIONS:
            while True:
                y += delta_y
                x += delta_x
                if y < 0 or x < 0:
                    return visit_places
                try:
                    if guard_map[y][x] == "#":
                        y -= delta_y
                        x -= delta_x
                        break
                    if (y, x) not in already_visited:
                        visit_places += 1
                        already_visited.append((y, x))
                except IndexError:
                    return visit_places


def main():
    guard_map = PUZZLE_INPUT
    #guard_map = INPUT_FILE.read_text(encoding="UTF-8").splitlines()
    print(count_visited_places(get_start_position(guard_map), guard_map))

    
if __name__ == '__main__':
    main()