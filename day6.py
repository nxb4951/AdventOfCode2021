# Day 6: Lanternfish
# Author: Nathan Bloom
import argparse


def lanternfish(input_file, days):
    fish_lst = [0 for _ in range(9)]
    with open(input_file) as input_file:
        for line in input_file:
            in_fish = [int(i) for i in line.split(",")]
            while len(fish_lst) <= max(in_fish):  # make sure the length is long enough
                fish_lst.append(0)
            for fish in in_fish:
                fish_lst[fish] += 1  # each index in the list represents how many fish have a timer spawning at that
                # index
    for i in range(days):
        reproducing = fish_lst[0]
        fish_lst = fish_lst[1:] + [0]
        fish_lst[8] += reproducing
        fish_lst[6] += reproducing
    return sum(fish_lst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 6 challenge: Lanternfish")  # argparser setup
    parser.add_argument("input", type=str, help="A file containing the fish")
    parser.add_argument("days", type=int, help="How many days to run the simulation for")
    args = parser.parse_args()

    fish1 = lanternfish(args.input, args.days)
    print(f"Result: {fish1} fish!")
