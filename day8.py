# Day 8 challenge: Seven Segment Search
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
# what each digit is made up of
distinguishers = [2, 4, 3, 7]  # if a segment has one of these lengths we know which digit it corresponds to


def part1(input_file):
    input_data = []
    with open(input_file) as input_file:
        for line in input_file:
            readouts, final = line.split("|")
            readouts = readouts.strip().split(" ")
            final = final.strip().split(" ")
            input_data.append([readouts, final])

    result = 0
    for [_, final] in input_data:
        for character in final:
            if len(character) in distinguishers:
                result += 1
    return result


def part2(input_file):
    input_data = []
    with open(input_file) as input_file:
        for line in input_file:
            readouts, final = line.split("|")
            readouts = readouts.strip().split(" ")
            final = final.strip().split(" ")
            input_data.append([readouts, final])

    results = []
    for [readouts, final] in input_data:
        decoded = ["." for _ in readouts]
        known = dict()
        while "." in decoded:
            for index, digit in enumerate(readouts):
                if len(digit) in distinguishers:
                    num = [segments.index(i) for i in segments if len(i) == len(digit)][0]
                    known[num] = set([i for i in digit])
                    decoded[index] = num
            try:
                # have to have this try because it's possible that we will find some characters we can't decode yet
                l = [i for i in known[4] if i not in known[1]]
                for index, digit in enumerate([i for i in readouts]):
                    if decoded[index] == ".":  # make sure we have to decode this character
                        if set(digit) in known.values():  # if we already know the value, no need to think too hard
                            for key, value in known.items():
                                if value == set(digit):
                                    num = key
                            decoded[index] = num
                        elif len(digit) == 5:  # the basic concept os that we look for digits that are subsets
                            # of the indicator digits or the L structure (think of the arm of the 4)
                            if set(l).issubset(set(digit)):
                                num = 5
                                known[num] = set([i for i in digit])
                                decoded[index] = num
                            elif known[1].issubset(set(digit)):
                                num = 3
                                known[num] = set([i for i in digit])
                                decoded[index] = num
                            else:
                                num = 2
                                known[num] = set([i for i in digit])
                                decoded[index] = num
                        elif len(digit) == 6:
                            if known[4].issubset(set(digit)):  # have to do this first because L is a subset of 4
                                num = 9
                                known[num] = set([i for i in digit])
                                decoded[index] = num
                            elif set(l).issubset(set(digit)):
                                num = 6
                                known[num] = set([i for i in digit])
                                decoded[index] = num
                            else:
                                num = 0
                                known[num] = set([i for i in digit])
                                decoded[index] = num
            except KeyError:
                pass

        readout = ""
        for index, digit in enumerate(final):
            for key, value in known.items():
                if value == set(digit):
                    readout += str(key)
                    break
        print(final, "->", readout)
        results.append(int(readout))
    return sum(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 8 challenge: Seven Segment Search")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the display information")
    args = parser.parse_args()

    result1 = part1(args.input)
    print(f"Part 1 result: {result1} appearances of 1, 4, 7, or 8")
    result2 = part2(args.input)
    print(f"Part 2 result: {result2}")
