from pathlib import Path
from more_itertools import chunked


def load_data():
    lines = Path("data/day05.txt").read_text().splitlines()
    seeds = [int(seed) for seed in lines[0].split(": ")[1].split()]
    maps = []
    d = []
    for line in lines[2:]:
        if line:
            if line[0].isalpha():
                d = []
            else:
                dest, source, rng = line.split()
                d.append((int(source), int(dest), int(rng)))
        else:
            maps.append(d)
    maps.append(d)
    return seeds, maps


def get_value(d: list, key: int) -> int:
    def mapper(v: int) -> int:
        for source, dest, rng in d:
            if source <= v <= source + rng:
                return dest + (v - source)
        return v

    return mapper(key)


def find_location(source_seed, maps) -> int:
    next_seed = source_seed
    for current_map in maps:
        next_seed = get_value(current_map, next_seed)
    return next_seed


def rearrange(sources):
    pairs = list(chunked(sources, 2))
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    sorted_pairs = [(start, start + n) for start, n in sorted_pairs]
    return sorted_pairs


def overlap(interval1, interval2) -> bool:
    start1, end1 = interval1
    start2, end2 = interval2
    intervals = {start1: interval1, start2: interval2}
    left_interval = intervals[min(start1, start2)]
    right_interval = intervals[max(start1, start2)]
    return left_interval[1] > right_interval[0]


def transform(source_seeds, transformations):
    new_seeds = set()
    for i, interval in enumerate(source_seeds):
        any_overlap = False
        for start, dest, rng in transformations:
            if overlap(interval, (start, start + rng)):
                new_start = max(interval[0], start)
                new_end = min(interval[1], start + rng)
                new_seeds.add((new_start + (dest - start), new_end + (dest - start)))
                if new_start != interval[0] and new_end != interval[1]:
                    remaining_start = interval[0]
                    remaining_end = start - 1
                    source_seeds.append((remaining_start, remaining_end))
                    remaining_start = start + rng
                    remaining_end = interval[1]
                    source_seeds.append((remaining_start, remaining_end))
                elif new_start != interval[0]:
                    remaining_start = interval[0]
                    remaining_end = new_start
                    source_seeds.append((remaining_start, remaining_end))
                elif new_end != interval[1]:
                    remaining_start = new_end
                    remaining_end = interval[1]
                    source_seeds.append((remaining_start, remaining_end))
                any_overlap = True
                break
        if not any_overlap:
            new_seeds.add(interval)
    return list(new_seeds)


def find_range(source_seeds, maps):
    for transformations in maps:
        source_seeds = transform(source_seeds, transformations)
    return source_seeds


def day05():
    source_seeds, maps = load_data()
    locations = [find_location(source_seed, maps) for source_seed in source_seeds]
    print(min(locations))
    source_seeds = rearrange(source_seeds)
    ranges = find_range(source_seeds, maps)
    print(min(start for start, end in ranges))


if __name__ == '__main__':
    day05()
