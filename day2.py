# Day 2 challenge: Dive!
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


def part1(input_name):
    depth, distance = 0, 0
    with open(input_name) as input_file:
        for line in input_file:
            cmd, num = line.split(" ")[:2]
            if cmd == "forward":
                distance += int(num)
            elif cmd == "down":
                depth += int(num)
            elif cmd == "up":
                depth -= int(num)
    return depth, distance


def part2(input_name):
    depth, distance, aim = 0, 0, 0
    with open(input_name) as input_file:
        for line in input_file:
            cmd, num = line.split(" ")[:2]
            if cmd == "forward":
                distance += int(num)
                depth += (int(num) * aim)
            elif cmd == "down":
                aim += int(num)
            elif cmd == "up":
                aim -= int(num)
    return depth, distance


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 2 challenge: Dive!")  # argparser setup
    parser.add_argument("input", type=str, help="A file containing the navigation commands")
    args = parser.parse_args()
    depth1, distance1 = part1(args.input)
    print(f"Part one results: Travelled {depth1} deep over {distance1} distance for a final result of "
          f"{depth1 * distance1}")
    depth2, distance2 = part2(args.input)
    print(f"Part two results: Travelled {depth2} deep over {distance2} distance for a final result of "
          f"{depth2 * distance2}")
