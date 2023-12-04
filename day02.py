from pathlib import Path
from dataclasses import dataclass


@dataclass
class Pick:
    count: int
    type: str


@dataclass
class Extraction:
    picks: list[Pick]


@dataclass
class Game:
    id: int
    extractions: list[Extraction]


def decode_pick(text: str) -> Pick:
    number, color = text.split(" ")
    return Pick(int(number), color)


def decode_extraction(text: str) -> Extraction:
    picks = [decode_pick(pick) for pick in text.split(", ")]
    return Extraction(picks)


def decode_game(line: str) -> Game:
    part1, part2 = line.split(": ")
    id_ = int(part1.split(" ")[-1])
    extractions = [decode_extraction(extraction) for extraction in part2.split("; ")]
    return Game(id_, extractions)


def load_games() -> list[Game]:
    lines = Path("data/day02.txt").read_text().split("\n")
    return [decode_game(line) for line in lines]


def valid_pick(pick: Pick) -> bool:
    match pick.type:
        case "red":
            return pick.count <= 12
        case "green":
            return pick.count <= 13
        case "blue":
            return pick.count <= 14


def valid_extraction(extraction: Extraction) -> bool:
    return all(valid_pick(pick) for pick in extraction.picks)


def valid_game(game: Game) -> bool:
    return all(valid_extraction(extraction) for extraction in game.extractions)


def all_counts(game: Game, type: str):
    return (pick.count for extraction in game.extractions for pick in extraction.picks if pick.type == type)


def power(game: Game) -> int:
    return max(all_counts(game, "red")) * max(all_counts(game, "green")) * max(all_counts(game, "blue"))


def day02():
    games = load_games()
    valid_ids = [game.id for game in games if valid_game(game)]
    print(sum(valid_ids))
    power_sets = [power(game) for game in games]
    print(sum(power_sets))


if __name__ == '__main__':
    day02()
