#!/usr/bin/env python3
from pathlib import Path
import re


INPUT = Path("/home/dennis/AoC/2023/Day4/input.txt")

EXAMPLE_LINES = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()


def parse_cards(input_lines):
    cards = {}
    for card in input_lines:
        card_number, numbers = card.split(":")
        my_numbers, winning_numbers = numbers.strip().split("|")
        my_numbers = set(map(int, re.findall(r"\d+", my_numbers)))
        winning_numbers = set(map(int, re.findall(r"\d+", winning_numbers)))
        cards[int(card_number.replace("Card ", ""))] = my_numbers & winning_numbers
    return cards


def calculate_points(winnings):
    return 2 ** (winnings - 1) if winnings >= 1 else 0


def update_number_of_cards(card_to_wins, wins, card_id):
    for extra_card in range(1, wins + 1):
        card_to_wins[card_id + extra_card] += card_to_wins[card_id]
    return card_to_wins


def main():
    cards = parse_cards(INPUT.read_text(encoding="UTF-8").splitlines())
    print(sum(calculate_points(len(winning)) for winning in cards.values()))
    cards = {int(card_id): len(win) for card_id, win in cards.items()}
    card_to_wins = {card_id: 1 for card_id, _ in enumerate(cards, 1)}
    for card_id, wins in cards.items():
        card_to_wins = update_number_of_cards(card_to_wins, wins, card_id)
    print(sum(card_to_wins.values()))


if __name__ == "__main__":
    main()
