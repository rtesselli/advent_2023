from pathlib import Path
import re


def load_data():
    return Path("data/day01.txt").read_text().split("\n")


def first_and_last_digit(line: str) -> int:
    digits = [digit for digit in line if digit.isnumeric()]
    return int(digits[0] + digits[-1])


def find_digits(lines: list[str]) -> list[int]:
    return [
        first_and_last_digit(line)
        for line in lines
    ]


def solve_value(value: str) -> str:
    if value.isnumeric():
        return value
    match value:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"


def first_and_last_digit_extended(line: str) -> int:
    matches = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
    return int(solve_value(matches[0]) + solve_value(matches[-1]))


def find_digits_extended(lines: list[str]) -> list[int]:
    return [
        first_and_last_digit_extended(line)
        for line in lines
    ]


def day01():
    lines = load_data()
    values = find_digits(lines)
    print(sum(values))
    values = find_digits_extended(lines)
    print(sum(values))


if __name__ == '__main__':
    day01()
