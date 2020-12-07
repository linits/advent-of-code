#!/usr/bin/env python3

# ================================================================================
# -- File:          day_06/06_code.py
# -- Project:       advent-of-code-2020
# -- Project URL:   https://adventofcode.com/2020/
# -- Create Date:   2020-12-06 11:49
# -- Author:        moosploit
# -- Company:       https://github.com/moosploit
# -- License:       MIT License | http://www.opensource.org/licenses/MIT
# ================================================================================

from functools import reduce

with open("06_data.txt") as file:
	groups = file.read().split("\n\n")

count_all_diff_answers = 0
count_all_same_answers = 0

for group in groups:
	count_all_diff_answers += len(set(group.replace("\n", "")))
	count_all_same_answers += len(reduce(set.intersection,
                                      map(set, group.split())))

print(f"\nPart One | Sum of anyone counts: {count_all_diff_answers}")
print(f"\nPart Two | Sum of same counts: {count_all_same_answers}")
