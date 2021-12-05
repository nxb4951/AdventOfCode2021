# Day 4: Giant Squid
# Author: Nathan Bloom nxb4951@rit.edu
import argparse
from dataclasses import dataclass


@dataclass
class Board:
    """Class for keeping track of the values and hits on a bingo board"""
    lines: list
    hits: list

    def __init__(self, lines):
        self.lines = lines
        self.hits = [[False for _ in i] for i in lines]

    def __repr__(self):
        result = ""
        for board_line, hit_line in zip(self.lines, self.hits):
            for board_entry, hit_entry in zip(board_line, hit_line):
                if hit_entry:
                    result += "X "
                else:
                    result += f"{str(board_entry)} "
            result += "\n"
        return result

    def play(self, move):
        """
        Plays a move on the board.
        :param move: The number called
        :return: True if the board has a hit, False otherwise
        """
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == move:
                    self.hits[i][j] = True
                    return True
        return False

    def has_won(self):
        """
        Determines if the board has won.
        :return: True of the board has won, False otherwise
        """
        # part 1: check rows
        for row in self.hits:
            if sum(row) == len(row):  # in this case sum returns the number of True values in the list
                return True
        # part 2: check columns
        for i in range(len(self.hits[0])):
            if sum([j[i] for j in self.hits]) == len(self.hits):
                return True
        return False

    def score(self, play):
        result = 0
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                if not self.hits[i][j]:
                    result += self.lines[i][j]
        return result * play


def part2(input_file):
    boards = []
    plays = []
    with open(input_file) as input_file:
        current_board = []
        for i, line in enumerate(input_file):
            line = line.strip()
            if i == 0:
                plays = [int(j) for j in line.split(",")]
            else:
                if line == "":  # if we are at the end of a board
                    if current_board:  # if there is a board already made
                        boards.append(Board(current_board))  # add it to the list
                    current_board = []  # clear out the current board
                else:
                    current_board.append([int(j) for j in line.split(" ") if
                                          j != ""])  # process the line into integers and add them to the current board
        if current_board:  # if there is a board already made
            boards.append(Board(current_board))  # add it to the list
    for play in plays:
        print(f"Calling number {play}!")
        to_remove = []
        for board in boards:
            board.play(play)
            if board.has_won():
                if len(boards) - len(to_remove) > 1:
                    to_remove.append(board)
                else:
                    return boards[0], boards[0].score(play)
        for board in to_remove:
            boards.remove(board)


def part1(input_file):
    boards = []
    plays = []
    with open(input_file) as input_file:
        current_board = []
        for i, line in enumerate(input_file):
            line = line.strip()
            if i == 0:
                plays = [int(j) for j in line.split(",")]
            else:
                if line == "":  # if we are at the end of a board
                    if current_board:  # if there is a board already made
                        boards.append(Board(current_board))  # add it to the list
                    current_board = []  # clear out the current board
                else:
                    current_board.append([int(j) for j in line.split(" ") if
                                          j != ""])  # process the line into integers and add them to the current board
        if current_board:  # if there is a board already made
            boards.append(Board(current_board))  # add it to the list
    winning_board = ""
    winning_play = -1
    for play in plays:
        if not winning_board:
            print(f"Calling number {play}!")
            for board in boards:
                board.play(play)
                if board.has_won():
                    winning_board = board
                    winning_play = play
                    break
        else:
            return winning_board, winning_board.score(winning_play)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 1 challenge: Sonar Sweep")  # argparser setup
    parser.add_argument("input", type=str, help="A file containing the sonar values")
    args = parser.parse_args()

    winner1, score1 = part1(args.input)
    print(f"Part 1 results: Winning board:\n{winner1}\nScore: {score1}")
    winner2, score2 = part2(args.input)
    print(f"Part 2 results: Losing board:\n{winner2}\nScore: {score2}")
