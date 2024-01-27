import numpy as np


def load_data():
    return np.loadtxt("data/day09.txt", dtype=int)


def predict(sequence):
    diffs = []
    curr = sequence
    while np.count_nonzero(curr):
        diffs.append(np.diff(curr))
        curr = diffs[-1]
    acc = 0
    for diff in reversed(diffs[:-1]):
        acc += diff[-1]
    acc += sequence[-1]
    forward = acc
    acc = 0
    for diff in reversed(diffs[:-1]):
        acc = diff[0] - acc
    acc = sequence[0] - acc
    return forward, acc


def day09():
    sequences = load_data()
    predictions = [predict(sequence) for sequence in sequences]
    print(sum(prediction[0] for prediction in predictions))
    print(sum(prediction[1] for prediction in predictions))


if __name__ == '__main__':
    day09()
