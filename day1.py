from pathlib import Path
import regex as re

EXAMPLE_LINES = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

INPUT = Path("/home/dennis/AoC/2023/Day1/input.txt")
STRING_TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

PATTERN = "|".join(STRING_TO_DIGIT.keys())


def replace_words(text):
    text_and_digits = re.findall(f"\d|{PATTERN}", text, overlapped=True)
    text_and_digits = "".join(text_and_digits)
    for word, digit in STRING_TO_DIGIT.items():
        text_and_digits = re.sub(word, digit, text_and_digits)
    return text_and_digits


def find_digit(text):
    text = replace_words(text)
    return "".join(digit for digit in text if digit.isdigit())


def split_digits(digits):
    return int("".join([digits[0], digits[-1]]))


def main():
    lines = INPUT.read_text(encoding="UTF-8").splitlines()
    digits = list(map(find_digit, lines))
    print(sum(list(map(split_digits, digits))))


if __name__ == "__main__":
    main()
