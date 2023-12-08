from pathlib import Path
from math import lcm


def load_data():
    lines = Path("data/day08.txt").read_text().splitlines()
    instructions = lines[0]
    graph = {}
    for line in lines[2:]:
        key, rest = line.split(" = ")
        graph[key] = tuple(rest[1:-1].split(", "))
    return instructions, graph


def traverse(instructions, graph):
    steps = 0
    curr_node = "AAA"
    while curr_node != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        if instruction == "L":
            curr_node = graph[curr_node][0]
        else:
            curr_node = graph[curr_node][1]
        steps += 1
    return steps


def traverse_ghost(instructions, graph, curr_node):
    steps = 0
    while not curr_node.endswith("Z"):
        instruction = instructions[steps % len(instructions)]
        if instruction == "L":
            curr_node = graph[curr_node][0]
        else:
            curr_node = graph[curr_node][1]
        steps += 1
    return steps


def traverse2(instructions, graph):
    starting_nodes = [node for node in graph.keys() if node.endswith("A")]
    steps = [traverse_ghost(instructions, graph, node) for node in starting_nodes]
    return lcm(*steps)


def day08():
    instructions, graph = load_data()
    steps = traverse(instructions, graph)
    print(steps)
    steps = traverse2(instructions, graph)
    print(steps)


if __name__ == '__main__':
    day08()
