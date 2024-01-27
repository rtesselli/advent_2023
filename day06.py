import re
from pathlib import Path
from math import prod


def load_data():
    lines = Path("data/day06.txt").read_text().splitlines()
    return [
        [int(value) for value in re.findall(r"\d+", line)]
        for line in lines
    ]


def run_attempts(max_time):
    return [wait_time * (max_time - wait_time) for wait_time in range(1, max_time)]


def run_all_runs(times, distances):
    return [run_attempts(max_time) for max_time in times]


def day06():
    times, distances = load_data()
    run_distances = run_all_runs(times, distances)
    counts = [
        sum(distance > target_distance for distance in distances)
        for distances, target_distance in zip(run_distances, distances)
    ]
    print(prod(counts))
    big_time = int("".join([str(value) for value in times]))
    big_distance = int("".join([str(value) for value in distances]))
    attempts = run_attempts(big_time)
    print(sum(distance > big_distance for distance in attempts))


if __name__ == '__main__':
    day06()
