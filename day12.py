# Day 12 challenge: Passage Pathing
# Author: Nathan Bloom
import argparse


def pathprint(arr):
    for path in arr:
        print(",".join(path))


def pathfinder_1(nodes, node, history):
    """
    A recursive function to determine paths that start at the start and end at the end
    :param nodes: the collection of node relations
    :param node:  the current node
    :param history: the list of nodes recently visited
    :return: a list of legitimate paths generated
    """
    results = []

    new_history = history + [node]
    if node == "end":
        return [new_history]
    for neighbor in nodes[node]:
        if neighbor != "start":
            if neighbor not in history or neighbor[0].isupper():
                # print(f"Visiting node {neighbor} from node {node}")
                new_results = pathfinder_1(nodes, neighbor, new_history)
                results.extend(new_results)
    return results


def pathfinder_2(nodes, node, history):
    """
    A recursive function to determine paths that start at the start and end at the end
    :param nodes: the collection of node relations
    :param node:  the current node
    :param history: the list of nodes recently visited
    :return: a list of legitimate paths generated
    """
    results = []

    new_history = history + [node]
    if node == "end":
        return [new_history]
    for neighbor in nodes[node]:
        if neighbor != "start":
            if neighbor[0].isupper():  # big cave - can visit however many times we want
                new_results = pathfinder_2(nodes, neighbor, new_history)
                results.extend(new_results)
            else:
                smalls = [i for i in new_history if i[0].islower()]
                has_two = False  # whether or not a small cave has already been visited twice in this path
                for i in smalls:
                    if smalls.count(i) > 1:
                        has_two = True
                        break
                if (has_two and new_history.count(neighbor) < 1) or (not has_two and new_history.count(neighbor) < 2):
                    # print(f"Visiting node {neighbor} from node {node}")
                    new_results = pathfinder_2(nodes, neighbor, new_history)
                    results.extend(new_results)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 12 challenge: Passage Pathing")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the cave connections")
    args = parser.parse_args()

    nodes = dict()
    with open(args.input) as input_file:
        for line in input_file:
            components = line.strip().split("-")
            if components[0] in nodes.keys():  # make sure that each node exists and has its neighbors in its value set
                nodes[components[0]].add(components[1])
            else:
                nodes[components[0]] = {components[1]}
            if components[1] in nodes.keys():
                nodes[components[1]].add(components[0])
            else:
                nodes[components[1]] = {components[0]}
    # print(nodes)
    paths_1 = pathfinder_1(nodes, "start", [])
    # pathprint(paths_1)
    print(f"Part 1 result: {len(paths_1)} paths")
    paths_2 = pathfinder_2(nodes, "start", [])
    # pathprint(paths_2)
    print(f"Part 2 result: {len(paths_2)} paths")
