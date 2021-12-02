# Day 1 challenge: sonar sweep
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


def part1(in_file):
    greater = 0
    with open(in_file) as in_file:
        last = -1
        for line in in_file:
            line_int = int(line)
            if 0 <= last < line_int:  # last is only negative at the very start, when we shouldn't count anything
                greater += 1
            last = line_int
    return greater


def part2(in_file):
    greater = 0
    with open(in_file) as in_file:
        ints = in_file.readlines()
        last = -1
        for trio in zip(ints, ints[1:], ints[2:]):
            trio_sum = sum([int(i) for i in trio])

            if 0 <= last < trio_sum:
                greater += 1
                print(f"{trio_sum}\tgreater")
            else:
                print(trio_sum)
            last = trio_sum
    return greater


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 1 challenge: Sonar Sweep")  # argparser setup
    parser.add_argument("input", type=str, help="A file containing the sonar values")
    args = parser.parse_args()

    result1 = part1(args.input)
    print(f"Part 1 result: Depth increases {result1} times.")
    result2 = part2(args.input)
    print(f"Part 2 result: Depth increases {result2} times.")
