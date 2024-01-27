from pathlib import Path
from collections import Counter
from functools import cmp_to_key


def load_data():
    lines = Path("data/day07.txt").read_text().splitlines()
    hands = [line.split()[0] for line in lines]
    bids = [line.split()[1] for line in lines]
    bids = [int(value) for value in bids]
    return hands, bids


def hand_type(hand: str) -> int:
    counts = Counter(hand)
    if counts.most_common()[0][1] == 5:
        return 1  # Five of a kind
    if counts.most_common()[0][1] == 4:
        return 2  # Four of a kind
    if counts.most_common()[0][1] == 3:
        if counts.most_common()[1][1] == 2:
            return 3  # Full house
        return 4  # Three of a kind
    if counts.most_common()[0][1] == 2:
        if counts.most_common()[1][1] == 2:
            return 5  # Two pair
        return 6  # One pair
    return 7  # High card


def hand_type2(hand: str) -> int:
    if "J" in hand:
        counts = Counter(hand)
        match counts["J"]:
            case 5:
                return hand_type("AAAAA")
            case _:
                del counts["J"]
                return hand_type(hand.replace("J", counts.most_common()[0][0]))
    return hand_type(hand)


def card_importance(card):
    match card:
        case "A":
            return 1
        case "K":
            return 2
        case "Q":
            return 3
        case "J":
            return 4
        case "T":
            return 5
        case v:
            return -int(v) + 100


def card_importance2(card):
    match card:
        case "A":
            return 1
        case "K":
            return 2
        case "Q":
            return 3
        case "T":
            return 4
        case "J":
            return 100000
        case v:
            return -int(v) + 100


def compare(hand1, hand2):
    if hand_type(hand1) != hand_type(hand2):
        return hand_type(hand1) - hand_type(hand2)
    for one, two in zip(hand1, hand2):
        if one != two:
            return card_importance(one) - card_importance(two)
    return 0


def compare2(hand1, hand2):
    if hand_type2(hand1) != hand_type2(hand2):
        return hand_type2(hand1) - hand_type2(hand2)
    for one, two in zip(hand1, hand2):
        if one != two:
            return card_importance2(one) - card_importance2(two)
    return 0


def day07():
    hands, bids = load_data()
    ordered_hands = list(reversed(sorted(hands, key=cmp_to_key(compare))))
    ranks = [ordered_hands.index(hand) + 1 for hand in hands]
    print(sum(bid * rank for bid, rank in zip(bids, ranks)))
    ordered_hands = list(reversed(sorted(hands, key=cmp_to_key(compare2))))
    ranks = [ordered_hands.index(hand) + 1 for hand in hands]
    print(sum(bid * rank for bid, rank in zip(bids, ranks)))


if __name__ == '__main__':
    day07()
