# Day 13 challenge: Transparent Origami
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


def pointprint(points):
    """
    Prints a nice neat graph of points
    :param points: A list of points stored as [x, y] values
    :return:
    """
    board = [[" " for _ in range(max([i[0] for i in points]) + 1)] for _ in range(max([i[1] for i in points]) + 1)]
    # boy howdy if this list comprehension works i will be so pleased with myself
    for point in points:
        board[point[1]][point[0]] = "#"
    for line in board:
        for ch in line:
            print(f"{ch} ", end="")
        print()
    print()


def part1(input_file):
    commands = []
    points = []
    with open(input_file) as input_file:
        blank = False
        for line in input_file:
            if blank:
                commands.append(line.strip().split(" ")[-1].split("="))
                commands[-1][1] = int(commands[-1][1])
            elif line == "\n":
                blank = True
            else:
                points.append([int(i) for i in line.split(",")])

    for command in commands:
        assert command[0] in {"x", "y"}  # make sure the command is a valid one
        if command[0] == "x":
            for i in range(len(points)):
                if points[i][0] > (command[1] - 1):
                    points[i][0] = command[1] - (points[i][0] - command[1])
        elif command[0] == "y":
            for i in range(len(points)):
                if points[i][1] > (command[1] - 1):
                    points[i][1] = command[1] - (points[i][1] - command[1])
        return len(set([tuple(i) for i in points]))


def part2(input_file):
    commands = []
    points = []
    with open(input_file) as input_file:
        blank = False
        for line in input_file:
            if blank:
                commands.append(line.strip().split(" ")[-1].split("="))
                commands[-1][1] = int(commands[-1][1])
            elif line == "\n":
                blank = True
            else:
                points.append([int(i) for i in line.split(",")])

    for command in commands:
        assert command[0] in {"x", "y"}  # make sure the command is a valid one
        if command[0] == "x":
            for i in range(len(points)):
                if points[i][0] > (command[1] - 1):
                    points[i][0] = command[1] - (points[i][0] - command[1])
        elif command[0] == "y":
            for i in range(len(points)):
                if points[i][1] > (command[1] - 1):
                    points[i][1] = command[1] - (points[i][1] - command[1])
    return points


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 13 challenge: Transparent Origami")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the dot coordinates and fold commands")
    args = parser.parse_args()

    result1 = part1(args.input)
    print(f"Part 1 result: {result1} points visible")
    result2 = part2(args.input)
    print(f"Part 2 result:")
    pointprint(result2)
