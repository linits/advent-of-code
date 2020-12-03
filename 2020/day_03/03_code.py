#!/usr/bin/env python3

# ================================================================================
# -- File:          day_03/03_code.py
# -- Project:       advent-of-code-2020
# -- Project URL:   https://adventofcode.com/2020/
# -- Create Date:   2020-12-03 12:21
# -- Author:        moosploit
# -- Company:       https://github.com/moosploit
# -- License:       MIT License | http://www.opensource.org/licenses/MIT
# ================================================================================

import math


def count_trees(go_right, go_down):
	map = []

	with open("03_data.txt") as data:
		lines = data.readlines()
		for line in lines:
			map_size = math.ceil(len(lines) * go_right / (len(line)-1))
			map.append(line.strip() * map_size)

	char_tree = "#"
	char_square = "."

	trees = 0
	squares = 0
	cursor = go_right
	count_map_lines = go_down

	for line in map[go_down::go_down]:
		if cursor <= len(line):
			# print(f"{count_map_lines} | {line}")
			char = line[cursor]
			if char is char_tree:
				trees += 1
			cursor += go_right
			count_map_lines += 1
	return trees


part_two = count_trees(1, 1) * count_trees(3, 1) * \
    count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)

print(f"\nPart One | Trees: {count_trees(3, 1)}")
print(f"\nPart Two | Trees: {part_two}")
