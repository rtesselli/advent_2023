import numpy as np
from pathlib import Path


def load_data():
    lines = Path("data/day10.txt").read_text().splitlines()
    matrix = np.matrix([list(line.strip()) for line in lines])
    return matrix


def traverse(pipes):
    def next_moves(row, col, visited):
        candidate_moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        curr_symbol = pipes[row, col]
        D, U, R, L = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        match curr_symbol:
            case "S":
                candidate_moves = [L, R, U, D]
            case "F":
                candidate_moves = [D, R]
            case "L":
                candidate_moves = [U, R]
            case "J":
                candidate_moves = [L, U]
            case "7":
                candidate_moves = [L, D]
            case "-":
                candidate_moves = [L, R]
            case "|":
                candidate_moves = [U, D]
        valid_moves = []
        for next_row, next_col in candidate_moves:
            destination_symbol = pipes[next_row, next_col]
            if (0 <= next_row < pipes.shape[0] and
                    0 <= next_col < pipes.shape[1] and
                    destination_symbol != '.' and
                    (next_row, next_col) not in visited
            ):
                if curr_symbol != "S":
                    valid_moves.append((next_row, next_col))
                else:
                    if (
                            destination_symbol in ("|F7") and (next_row, next_col) == U or
                            destination_symbol in ("|LJ") and (next_row, next_col) == D or
                            destination_symbol in ("-FL") and (next_row, next_col) == L or
                            destination_symbol in ("-J7") and (next_row, next_col) == R
                    ):
                        valid_moves.append((next_row, next_col))
        return valid_moves

    starting_point = np.where(pipes == 'S')
    starting_row, starting_col = starting_point
    frontier = [(starting_row[0], starting_col[0])]
    steps = 0
    visited = set()
    while frontier:
        next_frontier = []
        for row, col in frontier:
            if (row, col) in visited:
                return steps, visited
            visited.add((row, col))
            for next_row, next_col in next_moves(row, col, visited):
                next_frontier.append((next_row, next_col))
        steps += 1
        frontier = next_frontier
    return steps, visited


def solve_s(row, col, pipes):
    moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    D, U, R, L = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    checks = []
    for i, move in enumerate(moves):
        next_row, next_col = move
        if (0 <= next_row < pipes.shape[0] and
                0 <= next_col < pipes.shape[1]):
            if move == D:
                checks.append(pipes[next_row, next_col] in "|JL")
            elif move == U:
                checks.append(pipes[next_row, next_col] in "|7F")
            elif move == R:
                checks.append(pipes[next_row, next_col] in "-7J")
            elif move == L:
                checks.append(pipes[next_row, next_col] in "-FL")
            else:
                checks.append(False)
        else:
            checks.append(False)
    match checks:
        case [True, True, False, False]:
            return "|"
        case [False, False, True, True]:
            return "-"
        case [True, False, False, True]:
            return "7"
        case [False, True, False, True]:
            return "J"
        case [False, True, True, False]:
            return "L"
        case [True, False, True, False]:
            return "F"


def count_inner(pipes, path):
    starting_point = np.where(pipes == 'S')
    starting_row, starting_col = starting_point
    starting_row, starting_col = (starting_row[0], starting_col[0])
    actual_value = solve_s(starting_row, starting_col, pipes)
    pipes[pipes == "S"] = actual_value
    count = 0
    for row, line in enumerate(pipes):
        count_vertical = 0
        count_partial1 = 0
        count_partial2 = 0
        for col, value in enumerate(np.array(line).flatten()):
            if (row, col) in path:
                match value:
                    case "|":
                        count_vertical += 1
                    case "F":
                        count_partial1 += 0.5
                    case "L":
                        count_partial2 += 0.5
                    case "J":
                        count_partial1 += 0.5
                    case "7":
                        count_partial2 += 0.5
            else:
                inside = abs(count_vertical + count_partial1 - count_partial2) % 2 == 1
                count += 1 if inside else 0
    return count


def day10():
    pipes = load_data()
    max_distance, path = traverse(pipes)
    print(max_distance)
    inner = count_inner(pipes, path)
    print(inner)


if __name__ == '__main__':
    day10()
