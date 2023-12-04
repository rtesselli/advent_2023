import re
from pathlib import Path
from itertools import product


def load_data():
    lines = Path("data/day03.txt").read_text().split("\n")
    symbol_coords = set()
    number_coords = []
    gear_coords = set()
    for row_number, line in enumerate(lines):
        matches = re.finditer(r"(\d+|[^a-z\.])", line)
        for match in matches:
            match: re.Match
            value = match.group(0)
            if value.isnumeric():
                number_coords.append((int(value), (row_number, *match.span())))
            else:
                symbol_coords.add((row_number, match.start()))
                if value == '*':
                    gear_coords.add((row_number, match.start()))
    return symbol_coords, number_coords, gear_coords


def near_symbol(symbols, row, start, end) -> bool:
    return any(
        [coord in symbols for coord in product([row - 1, row + 1], range(start - 1, end + 1))] +
        [(row, start - 1) in symbols, (row, end) in symbols]
    )


def near_numbers(numbers, row, col):
    def adjacent(number_row, start, end):
        if number_row == row - 1 or number_row == row + 1:
            return col in range(start - 1, end + 1)
        if number_row == row:
            return col == start - 1 or col == end
        return False

    adjacent_numbers = [number for number, (number_row, start, end) in numbers if adjacent(number_row, start, end)]
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    return False


def day03():
    symbols, numbers, gears = load_data()
    part_numbers = [number for number, (row, start, end) in numbers if near_symbol(symbols, row, start, end)]
    print(sum(part_numbers))
    gear_rations = [ratio for row, col in gears if (ratio := near_numbers(numbers, row, col))]
    print(sum(gear_rations))


if __name__ == '__main__':
    day03()
