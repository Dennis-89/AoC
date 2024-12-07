#!/usr/bin/env python
from pathlib import Path
from itertools import cycle

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
    y, x = start_position
    already_visited = {(y, x)}
    for delta_y, delta_x in cycle(DIRECTIONS):
        while True:
            y += delta_y
            x += delta_x
            if y < 0 or x < 0:
                return len(already_visited)
            try:
                if guard_map[y][x] == "#":
                    y -= delta_y
                    x -= delta_x
                    break
            except IndexError:
                return len(already_visited)
            already_visited.add((y, x))


def main():
    guard_map = PUZZLE_INPUT
    #guard_map = INPUT_FILE.read_text(encoding="UTF-8").splitlines()
    print(count_visited_places(get_start_position(guard_map), guard_map))

    
if __name__ == '__main__':
    main()