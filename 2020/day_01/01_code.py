#!/usr/bin/env python3

# ================================================================================
# -- File:          day_01/01_code.py
# -- Project:       advent-of-code-2020
# -- Project URL:   https://adventofcode.com/2020/
# -- Create Date:   2020-12-03 10:54
# -- Author:        moosploit
# -- Company:       https://github.com/moosploit
# -- License:       MIT License | http://www.opensource.org/licenses/MIT
# ================================================================================

with open("01_data.txt") as data:
	lines = data.readlines()
	for x in lines:
		for y in lines:
			# === Part One === /
			if (int(x) + int(y) == 2020):
				a = int(x) * int(y)
				print(f"Part One | {int(x)} + {int(y)} | {a}")
			# === Part Two === /
			for z in lines:
				if (int(x) + int(y) + int(z) == 2020):
					b = int(x) * int(y) * int(z)
					print(f"Part Two | {int(x)} + {int(y)} + {int(z)} | {b}")
