# Day 17 challenge: Trick Shot
# Author: Nathan Bloom nxb4951@rit.edu
import argparse


def step(velocity, coordinates):
    """
    Helper function to determine the next coordinate and velocity measurement
    :param coordinates: The current coordinates of the probe
    :param velocity: The current velocity
    :return: The new velocity and coordinates of the probe
    """
    new_x_vel = velocity[0] - 1 if velocity[0] > 0 else (velocity[0] if velocity[0] == 0 else velocity[0] + 1)
    return (new_x_vel, velocity[1] - 1), (coordinates[0] + velocity[0], coordinates[1] + velocity[1])


def is_valid(start_x, start_y, target_x, target_y):
    current_point = (0, 0)
    starting_velocity = (start_x, start_y)
    current_velocity = starting_velocity
    max_y = 0
    while current_point[1] > min(target_y):
        current_velocity, current_point = step(current_velocity, current_point)
        # print(current_point)
        if current_point[1] > max_y:
            max_y = current_point[1]
        if current_point[0] in range(min(target_x), max(target_x) + 1) and current_point[1] in \
                range(min(target_y), max(target_y) + 1):
            return True
    return False


def part1(input_file):
    with open(input_file) as input_file:
        line = input_file.readline()
        target_x = [int(i) for i in line.strip().split(" ")[2].lstrip("x=").rstrip(",").split("..")]
        target_y = [int(i) for i in line.strip().split(" ")[3].lstrip("y=").rstrip(",").split("..")]

    valid_paths = dict()  # each key will be the highest y point reached, each value will be the starting velocity
    for start_x in range(max(target_x)):
        for start_y in range(1000):
            current_point = (0, 0)
            starting_velocity = (start_x, start_y)
            current_velocity = starting_velocity
            max_y = 0
            while current_point[1] > min(target_y):
                # eventually we'll fall out of range, at which point the path will be invalid if we haven't already
                # ended up in the target zone
                current_velocity, current_point = step(current_velocity, current_point)
                if current_point[1] > max_y:
                    max_y = current_point[1]
                if current_point[0] in range(target_x[0], target_x[1]) and current_point[1] in range(target_y[0],
                                                                                                     target_y[1]):
                    valid_paths[max_y] = starting_velocity
                    print(f"Valid velocity found: {start_x}, {start_y}, max height = {max_y}")

    return max(valid_paths.keys())


def part2(input_file):
    with open(input_file) as input_file:
        line = input_file.readline()
        target_x = [int(i) for i in line.strip().split(" ")[2].lstrip("x=").rstrip(",").split("..")]
        target_y = [int(i) for i in line.strip().split(" ")[3].lstrip("y=").rstrip(",").split("..")]

    valid_paths = 0  # use a set for more speed
    for start_x in range(max(target_x) + 1):
        for start_y in range(min(target_y), 1000):
            # i don't have a good reason for picking this upper bound but it works
            if is_valid(start_x, start_y, target_x, target_y):
                valid_paths += 1
                print(f"Valid velocity found: {start_x}, {start_y}")

    return valid_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 17 challenge: Trick Shot")
    # argparser setup
    parser.add_argument("input", type=str, help="A file containing the coordinates of the target area")
    args = parser.parse_args()

    result1 = part1(args.input)
    print(f"Part 1 result: {result1}")
    result2 = part2(args.input)  # more than 1674
    print(f"Part 2 result: {result2}")
