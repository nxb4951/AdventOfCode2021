# Day 5: Hydrothermal Venture
# Author: Nathan Bloom
import argparse


def print_board(board):
    for line in board:
        for ch in line:
            if ch != 0:
                print(ch, end=" ")
            else:
                print(". ", end="")
        print()


def part1(input_file):
    lines = set()
    with open(input_file) as input_file:
        for line in input_file:
            lines.add(
                (tuple([int(i) for i in line.split(" ")[0].split(",")]), tuple([int(i) for i in line.split(" ")[-1].split(",")])))

    to_remove = set()
    size = 0
    for line in lines:  # go through and figure out which lines aren't valid for part 1...
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            print(f"Line {line} is not valid for part 1")
            to_remove.add(line)
        else:  # sneaking in size detection in this loop
            size = max(size, max(max(line[0]), max(line[1])))
    for line in to_remove:  # ...and remove them
        # (have to do this separately because python throws a fit if you change a collection while iterating over it)
        lines.remove(line)
    size += 1  # zero-index errors are fun
    board = [[0 for _ in range(size)] for _ in range(size)]
    for line in lines:
        start, end = line
        if start[0] == end[0]:  # if the line is vertical
            x = start[0]
            start_ind = min(start[1], end[1])
            end_ind = max(start[1], end[1]) + 1
            for i in range(start_ind, end_ind):
                board[i][x] += 1
        else:
            y = start[1]
            start_ind = min(start[0], end[0])
            end_ind = max(start[0], end[0]) + 1
            for i in range(start_ind, end_ind):
                board[y][i] += 1

    score = 0
    for line in board:
        score += len([i for i in line if i > 1])

    return board, score


def part2(input_file):
    lines = set()
    with open(input_file) as input_file:
        for line in input_file:
            lines.add(
                (tuple([int(i) for i in line.split(" ")[0].split(",")]),
                 tuple([int(i) for i in line.split(" ")[-1].split(",")])))

    size = 0
    for line in lines:  # figure out board size
        size = max(size, max(max(line[0]), max(line[1])))
    size += 1  # zero-index errors are fun
    board = [[0 for _ in range(size)] for _ in range(size)]
    for line in lines:
        start, end = line
        if start[0] == end[0]:  # if the line is vertical
            x = start[0]
            start_ind = min(start[1], end[1])
            end_ind = max(start[1], end[1]) + 1
            for i in range(start_ind, end_ind):
                board[i][x] += 1
        elif start[1] == end[1]:  # if the line is horizontal
            y = start[1]
            start_ind = min(start[0], end[0])
            end_ind = max(start[0], end[0]) + 1
            for i in range(start_ind, end_ind):
                board[y][i] += 1
        else:
            current_point = start
            while True:
                board[current_point[0]][current_point[1]] += 1
                if current_point[0] < end[0] and current_point[1] < end[1]:
                    current_point = current_point[0] + 1, current_point[1] + 1
                elif current_point[0] < end[0] and current_point[1] > end[1]:
                    current_point = current_point[0] + 1, current_point[1] - 1
                elif current_point[0] > end[0] and current_point[1] < end[1]:
                    current_point = current_point[0] - 1, current_point[1] + 1
                elif current_point[0] > end[0] and current_point[1] > end[1]:
                    current_point = current_point[0] - 1, current_point[1] - 1
                if current_point == end:
                    board[current_point[0]][current_point[1]] += 1
                    break

    score = 0
    for line in board:
        score += len([i for i in line if i > 1])

    return board, score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 1 challenge: Sonar Sweep")  # argparser setup
    parser.add_argument("input", type=str, help="A file containing the sonar values")
    args = parser.parse_args()

    board1, score1 = part1(args.input)
    print(f"Part 1 results: Board:")
    # print_board(board1)
    print(f"Score: {score1}")
    board2, score2 = part2(args.input)
    print(f"Part 2 results: Board:")
    print_board(board2)
    print(f"Score: {score2}")
