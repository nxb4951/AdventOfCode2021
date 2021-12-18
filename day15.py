# Day 15 challenge: Chiton
# Author: Nathan Bloom nxb4951@rit.edu
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional


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


@dataclass
class Node:
    x: int
    y: int
    rating: int
    path_cost: Optional[int]
    last: Node

    def __init__(self, x, y, rating):
        self.x = x
        self.y = y
        self.rating = rating
        self.path_cost = None
        if x == 0 and y == 0:  # if we're at the starting point
            self.last = self
            self.path_cost = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Node({self.x}, {self.y})"

    def set_cost(self, board):
        if self.x == 0 and self.y == 0:  # if this is the starting point the cost is already set
            return
        lowest_cost = -1
        neighbors = []
        for y1 in range(self.y - 1, self.y + 2):
            for x1 in range(self.x - 1, self.x + 2):
                if ((self.x != x1 and self.y == y1) or (self.x == x1 and self.y != y1)) and min(x1, y1) >= 0:
                    try:
                        neighbors.append(board[y1][x1])
                    except IndexError:
                        pass

        for neighbor in neighbors:
            if (neighbor.path_cost is not None) and (neighbor.path_cost < lowest_cost or lowest_cost == -1):
                lowest_cost = neighbor.path_cost
                self.last = neighbor
        self.path_cost = lowest_cost + self.rating


def boardprint(board):
    for line in board:
        print("".join([str(i) for i in line]))


def pathprint(board):
    points = [(0, 0)]
    current_node = board[-1][-1]
    while current_node != board[0][0]:
        points.append((current_node.x, current_node.y))
        current_node = current_node.last
    for line in board:
        for current_node in line:
            if (current_node.x, current_node.y) in points:
                print(f"{Bcolors.OKBLUE}{current_node.rating}{Bcolors.ENDC}", end="")
            else:
                print(current_node.rating, end="")
        print()


def part2(input_file):
    original_board = []
    board = []
    with open(input_file) as input_file:
        for line in input_file:
            original_board.append([int(i) for i in line.strip()])

    offsets = []  # these will tell how much to increment each tile by
    for i in range(5):
        offsets.append([i + j for j in range(5)])

    for o_line in offsets:  # build the new array of danger values
        tile_line = []
        for offset in o_line:
            tile = [[(j + offset if j + offset < 10 else j + offset - 9) for j in line] for line in original_board]
            tile_line.append(tile)

        for i in range(len(tile_line[0])):
            board_row = []
            for j in tile_line[:5]:
                board_row.extend(j[i])
            board.append(board_row)

    nodes = []
    for y in range(len(board)):
        line = []
        for x in range(len(board[0])):
            line.append(Node(x, y, board[y][x]))
        nodes.append(line)

    changed = True
    while changed:
        changed = False
        for line in nodes:
            for node in line:
                old_cost = node.path_cost
                node.set_cost(nodes)
                if old_cost != node.path_cost:
                    changed = True

    return nodes[-1][-1].path_cost


def part1(input_file):
    board = []
    with open(input_file) as input_file:
        for line in input_file:
            board.append([int(i) for i in line.strip()])
    nodes = []
    for y in range(len(board)):
        line = []
        for x in range(len(board[0])):
            line.append(Node(x, y, board[y][x]))
        nodes.append(line)

    changed = True
    while changed:
        changed = False
        for line in nodes:
            for node in line:
                old_cost = node.path_cost
                node.set_cost(nodes)
                if old_cost != node.path_cost:
                    changed = True

    return nodes[-1][-1].path_cost


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 14 challenge: Extended Polymerization")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the danger levels at each coordinate")
    args = parser.parse_args()

    result1 = part1(args.input)
    print(f"Part 1 result: {result1}")
    result2 = part2(args.input)
    print(f"Part 2 result: {result2}")
