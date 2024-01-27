from pathlib import Path


def load_cards():
    lines = Path("data/day04.txt").read_text().splitlines()
    lines = [line.split(":")[1].strip() for line in lines]
    extracted = [{value for value in line.split("|")[0].split(" ") if value} for line in lines]
    played = [{value for value in line.split("|")[1].split(" ") if value} for line in lines]
    return extracted, played


def day04():
    extracted, played = load_cards()
    wins = [len(e & p) for e, p in zip(extracted, played)]
    print(sum(2 ** (count - 1) for count in wins if count))
    counts = [1] * len(extracted)
    for current, win in enumerate(wins):
        for offset in range(1, win + 1):
            counts[current + offset] += counts[current]
    print(sum(counts))


if __name__ == '__main__':
    day04()
