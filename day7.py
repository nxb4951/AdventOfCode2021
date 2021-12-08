# Day 7: The Treachery of Whales
# Author: Nathan Bloom
import argparse


def part1(input_file):
    crabs = []
    with open(input_file) as input_file:
        for line in input_file:
            crabs.extend([int(i) for i in line.split(",")])

    for target_position in range(max(crabs)):
        fuel = sum([abs(i - target_position) for i in crabs])
        try:
            if fuel < best_fuel:
                best_fuel = fuel
                best_position = target_position
        except NameError:
            # hacky way around not defining best fuel at first, since we're looking for a number closest to zero
            best_position = target_position
            best_fuel = fuel

    return best_position, best_fuel


def part2(input_file):
    crabs = []
    with open(input_file) as input_file:
        for line in input_file:
            crabs.extend([int(i) for i in line.split(",")])

    for target_position in range(max(crabs)):
        fuel = sum([((0.5 * abs(i - target_position)) + (0.5 * abs(i - target_position) * (abs(i - target_position)))) for i in crabs])
        try:
            if fuel < best_fuel:
                best_fuel = fuel
                best_position = target_position
        except NameError:
            best_position = target_position
            best_fuel = fuel

    return best_position, best_fuel


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 7 challenge: The Treachery of Whales")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the crab positions")
    args = parser.parse_args()

    position1, fuel1 = part1(args.input)
    print(f"Part 1 results: {position1} is most efficient, consuming {fuel1} fuel.")
    position2, fuel2 = part2(args.input)
    print(f"Part 2 results: {position2} is most efficient, consuming {fuel2} fuel.")
