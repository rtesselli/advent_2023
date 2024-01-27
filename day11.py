import numpy as np
from pathlib import Path


def load_data():
    lines = Path("data/day11.txt").read_text().splitlines()
    matrix = np.matrix([list(line.strip()) for line in lines])
    return matrix


def find_empties(universe):
    numbers = np.empty_like(universe, dtype=int)
    numbers[universe == '.'] = 0
    numbers[universe == '#'] = 1
    rows = np.where(np.sum(numbers, axis=1) == 0)[0]
    cols = np.where(np.sum(numbers, axis=0) == 0)[1]
    return set(rows), set(cols)


def compute_distances(universe, empty_rows, empty_cols, factor=1):
    distances = []
    rows, cols = np.where(universe == '#')
    for i, (row1, col1) in enumerate(zip(rows, cols)):
        for row2, col2 in zip(rows[i+1:], cols[i+1:]):
            distance = abs(row1 - row2) + abs(col1 - col2)
            extra_rows = sum(factor for empty in empty_rows if empty in range(min(row1, row2), max(row1, row2) + 1))
            extra_cols = sum(factor for empty in empty_cols if empty in range(min(col1, col2), max(col1, col2) + 1))
            distances.append(distance + extra_rows + extra_cols)
    return distances


def day11():
    universe = load_data()
    empty_rows, empty_cols = find_empties(universe)
    distances = compute_distances(universe, empty_rows, empty_cols)
    print(sum(distances))
    distances = compute_distances(universe, empty_rows, empty_cols, factor=1000000-1)
    print(sum(distances))


if __name__ == '__main__':
    day11()
