# Day 11 challenge: Dumbo Octopus
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def octoprint(arr):
    for line in arr:
        for ch in line:
            if ch == 0:
                print(Bcolors.WARNING + str(ch) + Bcolors.ENDC, end="")
            else:
                print(ch, end="")
        print()


def part1(input_file, iterations):
    octo = []
    with open(input_file) as input_file:
        for line in input_file:
            octo.append([int(i) for i in line.strip()])
    print("Initial state: ")
    octoprint(octo)
    flashes = 0
    for j in range(iterations):
        flashing = []
        for y in range(len(octo)):
            for x in range(len(octo[0])):
                octo[y][x] += 1
                if octo[y][x] > 9:
                    flashing.append((y, x))
                    octo[y][x] = 0
                    flashes += 1
        while flashing:
            new_flash = []
            for i in range(len(flashing)):
                y, x = flashing[i]
                for y1 in [i for i in [y - 1, y, y + 1] if (0 <= i < len(octo))]:
                    for x1 in [i for i in [x - 1, x, x + 1] if 0 <= i < len(octo[0])]:
                        if (y != y1 or x != x1) and octo[y1][x1] != 0:
                            if octo[y1][x1] == 9:
                                new_flash.append((y1, x1))
                                octo[y1][x1] = 0
                                flashes += 1
                            else:
                                octo[y1][x1] += 1

            flashing = new_flash
        print(f"\nRound {j + 1}:")
        octoprint(octo)
    return flashes


def part2(input_file):
    octo = []
    with open(input_file) as input_file:
        for line in input_file:
            octo.append([int(i) for i in line.strip()])
    print("Initial state: ")
    octoprint(octo)
    flashes = 0
    ctr = 0
    while sum([sum(i) for i in octo]) != 0:
        flashing = []
        for y in range(len(octo)):
            for x in range(len(octo[0])):
                octo[y][x] += 1
                if octo[y][x] > 9:
                    flashing.append((y, x))
                    octo[y][x] = 0
                    flashes += 1
        while flashing:
            new_flash = []
            for i in range(len(flashing)):
                y, x = flashing[i]
                for y1 in [i for i in [y - 1, y, y + 1] if (0 <= i < len(octo))]:
                    for x1 in [i for i in [x - 1, x, x + 1] if 0 <= i < len(octo[0])]:
                        if (y != y1 or x != x1) and octo[y1][x1] != 0:
                            if octo[y1][x1] == 9:
                                new_flash.append((y1, x1))
                                octo[y1][x1] = 0
                                flashes += 1
                            else:
                                octo[y1][x1] += 1

            flashing = new_flash
        print(f"\nRound {ctr + 1}:")
        octoprint(octo)
        ctr += 1
    return ctr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 11 challenge: Dumbo Octopus")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the octopus layout")
    parser.add_argument("iterations", type=int, help="How many rounds to simulate")
    args = parser.parse_args()

    result1 = part1(args.input, args.iterations)
    print(f"Part 1 result: {result1} flashes")
    result2 = part2(args.input)
    print(f"Part 2 result {result2} rounds")
