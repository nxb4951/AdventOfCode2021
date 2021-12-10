# Day 9 Challenge: Smoke Basin
# Author: Nathan Bloom
import argparse


def part1(input_file):
    topology = []
    with open(input_file) as input_file:
        for line in input_file:
            topology.append([int(i) for i in line.strip()])
    low_points = []
    for y in range(len(topology)):
        for x in range(len(topology[0])):
            # print(topology[y][x])
            is_low_point = True
            if x > 0 and topology[y][x] >= topology[y][x - 1]:
                is_low_point = False
            if y > 0 and topology[y][x] >= topology[y - 1][x]:
                is_low_point = False
            if x < len(topology[0]) - 1:
                if topology[y][x] >= topology[y][x + 1]:
                    is_low_point = False
            if y < len(topology) - 1:
                if topology[y][x] >= topology[y + 1][x]:
                    is_low_point = False
            if is_low_point:
                low_points.append([x, y, topology[y][x]])
    return sum([i[2] + 1 for i in low_points])


def get_adjacent_points(x, y, topology):
    """
    small function to get a list of points around the current point
    :param x: x-val of current point
    :param y: y-val of current point
    :param topology: topology to interrogate
    :return: a list of surrounding points as [x, y, z]
    """
    surrounding = []
    if x > 0:
        surrounding.append([x - 1, y, topology[y][x - 1]])
    if y > 0:
        surrounding.append([x, y - 1, topology[y - 1][x]])
    if x < len(topology[0]) - 1:
        surrounding.append([x + 1, y, topology[y][x + 1]])
    if y < len(topology) - 1:
        surrounding.append([x, y + 1, topology[y + 1][x]])
    return surrounding


def part2(input_file):
    topology = []
    with open(input_file) as input_file:
        for line in input_file:
            topology.append([int(i) for i in line.strip()])
    low_points = []
    for y in range(len(topology)):
        for x in range(len(topology[0])):
            # print(topology[y][x])
            is_low_point = True
            if x > 0 and topology[y][x] >= topology[y][x - 1]:
                is_low_point = False
            if y > 0 and topology[y][x] >= topology[y - 1][x]:
                is_low_point = False
            if x < len(topology[0]) - 1:
                if topology[y][x] >= topology[y][x + 1]:
                    is_low_point = False
            if y < len(topology) - 1:
                if topology[y][x] >= topology[y + 1][x]:
                    is_low_point = False
            if is_low_point:
                low_points.append([x, y, topology[y][x]])
    # print(low_points)

    basins = []  # this will hold values for the sizes of each basin
    for point in low_points:
        x, y, depth = point
        basin_points = {tuple(point)}
        to_visit = get_adjacent_points(x, y, topology)
        while len(to_visit) != 0:
            adj_point = to_visit.pop()
            if adj_point[2] != 9 and tuple(adj_point) not in basin_points:
                # make sure that the point hasn't been visited and isn't too tall
                basin_points.add(tuple(adj_point))
                to_visit.extend([i for i in get_adjacent_points(adj_point[0], adj_point[1], topology) if tuple(i) not in basin_points])
        # print(basin_points)
        basins.append(len(basin_points))
    basins.sort(reverse=True)
    # print(basins[:3])
    product = 1
    for i in basins[:3]:
        product *= i
    return product


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 9 challenge: Smoke Basin")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the topology information")
    args = parser.parse_args()

    result1 = part1(args.input)
    print(f"Part 1 result: Low point risk levels = {result1}")
    result2 = part2(args.input)
    print(f"Part 2 result: Product of largest basins = {result2}")  # not 14904
