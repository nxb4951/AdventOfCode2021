# Day 3 challenge: Binary Diagnostic
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


def part1(input_file):
    ones = []
    lines = 0
    with open(input_file) as input_file:
        for line in input_file:
            lines += 1
            if not ones:
                ones = [0] * (len(line) - 1)
            for i in range(len(line)):
                if line[i] == "1":
                    ones[i] += 1

    gamma, epsilon = "", ""
    for i in ones:
        if i > lines // 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2), int(epsilon, 2)


def part2(input_file):
    valid_oxygen, valid_carbon = [], []
    with open(input_file) as input_file:  # read the elements into lists
        for line in input_file:
            valid_oxygen.append(line.strip())
            valid_carbon.append(line.strip())

    length_to_check = len(valid_oxygen[0])
    for i in range(length_to_check):  # i is the index of the element to check
        if len(valid_oxygen) > 1:
            one_ctr = len([j for j in valid_oxygen if j[i] == "1"])  # this counts the number of elements with 1 in
            # the position we are interested in
            check = "1" if (one_ctr >= (len(valid_oxygen) / 2)) else "0"
            valid_oxygen = [j for j in valid_oxygen if j[i] == check]  # now remake valid oxygen with only the
            # elements we care about

    for i in range(len(valid_carbon[0])):  # do the same for carbon
        if len(valid_carbon) > 1:
            one_ctr = len([j for j in valid_carbon if j[i] == "1"])
            check = "0" if (one_ctr >= len(valid_carbon) / 2) else "1"
            valid_carbon = [j for j in valid_carbon if j[i] == check]
    return int(valid_oxygen[0], 2), int(valid_carbon[0], 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 3 challenge: Binary Diagnostic")  # argparser setup
    parser.add_argument("input", type=str, help="A file containing the binary readouts")
    args = parser.parse_args()

    gamma1, epsilon1 = part1(args.input)
    print(f"Part one result: Gamma = {gamma1}, epsilon = {epsilon1}, final result = {gamma1 * epsilon1}")
    oxygen, carbon = part2(args.input)
    print(f"Part two result: Oxygen = {oxygen}, carbon = {carbon}, life support rating = {oxygen * carbon}")
