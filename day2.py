from pathlib import Path
from functools import reduce
import re

EXAMPLE_LINES = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

INPUT = Path('/home/dennis/AoC/2023/Day2/input.txt')
MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_input(game):
    id_separated = [item.strip() for item in game.split(':')]
    color_with_numbers = []
    for game_round in id_separated[1].split(';'):
        color_with_numbers.extend(
            {color.strip().replace(',', ''): int(number)}
            for number, color in zip(
                re.findall(r'\d+', game_round.strip()),
                re.findall(r'\D+', game_round.strip())
                )
        )
    return {int(id_separated[0].replace('Game ', '')): color_with_numbers}


def get_min_cubes(game):
    biggest_number = {}
    for cubes in game.values():
        for pair in cubes:
            for color, number in pair.items():
                if color in biggest_number and biggest_number[color] < number:
                    biggest_number[color] = number
                elif color not in biggest_number:
                    biggest_number[color] = number
    return biggest_number


def get_sum_of_powers_produces(games):
    powers_produces = []
    for game in games:
        if game:
            color_to_fewest_number = get_min_cubes(game)
            powers_produces.append(reduce(lambda x, y: x * y, list(color_to_fewest_number.values())))
    return sum(powers_produces)


def get_sum_of_possible_games(games):
    id_of_impossible_games = []
    for game in games:
        for game_id, cubes in game.items():
            for color_to_number in cubes:
                for color, number in color_to_number.items():
                    if (
                            number > MAX_CUBES[color]
                            and game_id not in id_of_impossible_games
                    ):
                        id_of_impossible_games.append(game_id)
    for game in games:
        for impossible_games in id_of_impossible_games:
            game.pop(impossible_games, None)
    possible_games = []
    for game in games:
        possible_games.extend(iter(game.keys()))
    return sum(possible_games)


def main():
    games = [parse_input(game) for game in INPUT.read_text(encoding='UTF-8').splitlines()]
    print(get_sum_of_powers_produces(games))
    print(get_sum_of_possible_games(games))


if __name__ == '__main__':
    main()