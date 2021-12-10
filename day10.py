# Day 10 challenge: Syntax Scoring
# Author: Nathan Bloom nxb4951@rit.edu
import argparse

relations = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}


p1_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

p2_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def part1(input_file):
    with open(input_file) as input_file:
        lines = input_file.readlines()

    errors = []
    for index, line in enumerate([i.strip() for i in lines]):
        closers = []  # contains the closing brackets expected
        for ch in line:
            if ch in relations.keys():  # if it's an opening bracket
                closers = [relations[ch]] + closers  # add its respective closing bracket to the list
            elif closers[0] == ch:  # if the bracket is the one we expect
                closers = closers[1:]
            else:
                print(f"Error on line {index}: Expected {closers[0]}, got {ch}")
                errors += ch
                break
    return sum([p1_points[i] for i in errors])


def part2(input_file):
    with open(input_file) as input_file:
        lines = input_file.readlines()

    errors = []
    scores = []
    for index, line in enumerate([i.strip() for i in lines]):
        closers = []  # contains the closing brackets expected
        has_error = False
        for ch in line:
            if ch in relations.keys():  # if it's an opening bracket
                closers = [relations[ch]] + closers  # add its respective closing bracket to the list
            elif closers[0] == ch:  # if the bracket is the one we expect
                closers = closers[1:]
            else:
                errors += ch
                has_error = True
                break

        if closers and not has_error:
            score = 0
            for ch in closers:
                score *= 5
                score += p2_points[ch]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 10 challenge: Syntax Scoring")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the navigation subsystem")
    args = parser.parse_args()

    score1 = part1(args.input)
    print(f"Part 1 result: {score1}")
    score2 = part2(args.input)
    print(f"Part 2 result: {score2}")
