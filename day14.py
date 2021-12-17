# Day 14 challenge: Extended Polymerization
# Author: Nathan Bloom
import argparse
from collections import defaultdict, Counter
from functools import lru_cache


rules = dict()


@lru_cache
def expand(template, step):
    """
    Recursively expands the polymer (will find the solution... eventually...)
    :param template: The pair to insert with
    :param step: The number of steps to be run
    :return: A dictionary containing the counts of each element
    """
    results = defaultdict(int)
    if step == 1:
        # print(rules[template], end="")
        results[rules[template]] += 1

        assert min(results.values()) >= 0
        return results
    else:
        results[rules[template]] += 1
        template = template[0] + rules[template] + template[1]
        for t1, t2 in zip(template, template[1:]):
            pair_results = expand(t1 + t2, step - 1)

            for i in pair_results.keys():
                results[i] += pair_results[i]

        assert min(results.values()) >= 0
        return results


def expand_loop(pairs, template, steps):
    """
    Uses loops instead of recursion to find the solution. Works way faster than the original method.
    :param pairs: The starting pairs
    :param template: The starting polymer template
    :param steps: The number of steps to be run
    :return: The difference between the most common and least common elements
    """
    for i in range(steps):
        new_pairs = Counter()
        for pair in pairs:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs

    letters = Counter()
    for pair in pairs:
        letters[pair[0]] += pairs[pair]
    letters[template[-1]] += 1
    return max(letters.values()) - min(letters.values())


def part1(input_file, step):
    template = ""
    global rules
    with open(input_file) as input_file:
        for line in input_file:
            if not template:
                template = line.strip()
            elif line != "\n":
                rule, _, add = line.strip().split(" ")
                rules[rule] = add
    # print(template, "\n", rules)
    # results = defaultdict(int)
    # for t1, t2 in zip(template, template[1:]):
    #     pair_results = expand(t1 + t2, step)
    #     results[t1] += 1
    #     for i in pair_results.keys():
    #         results[i] += pair_results[i]
    # results[t2] += 1  # since we actually have to count both the start and end of the last pair
    # print(results)
    # return max(results.values()) - min(results.values())
    pairs = Counter()
    for i in range(len(template) - 1):
        pairs[template[i] + template[i + 1]] += 1
    return expand_loop(pairs, template, step)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 14 challenge: Extended Polymerization")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the template polymer and pair insertion rules")
    parser.add_argument("steps", type=int, help="How many steps to run the simulation for")
    args = parser.parse_args()

    result = part1(args.input, args.steps)
    print(f"Result: {result}")
