#!/usr/bin/env python3

# ================================================================================
# -- File:          day_05/05_code.py
# -- Project:       advent-of-code-2020
# -- Project URL:   https://adventofcode.com/2020/
# -- Create Date:   2020-12-05 18:41
# -- Author:        moosploit
# -- Company:       https://github.com/moosploit
# -- License:       MIT License | http://www.opensource.org/licenses/MIT
# ================================================================================

import math

seats = {}


def find_seat(seat):
	index = 0

	row = -1
	first_row = 0
	last_row = 127

	column = -1
	first_col = 0
	last_col = 7

	mid = 0

	while(index < len(seat)):
		if (index <= 6):
			mid = (first_row+last_row)/2
			if(seat[index] == "F"):
				last_row = math.floor(mid)
				if (first_row == last_row):
					row = last_row
			elif(seat[index] == "B"):
				first_row = math.ceil(mid)
				if (first_row == last_row):
					row = first_row
		else:
			mid = (first_col+last_col)/2
			if(seat[index] == "R"):
				first_col = math.ceil(mid)
				if (first_col == last_col):
					column = first_col
			elif(seat[index] == "L"):
				last_col = math.floor(mid)
				if (first_col == last_col):
					column = last_col
		index += 1

	seat_id = row * 8 + column
	return seat_id, row, column


with open("05_data.txt") as file:
	boardingpasses = file.readlines()

for boardingpass in boardingpasses:
	seat_id, seat_row, seat_col = find_seat(boardingpass.strip())
	seats[seat_id] = [seat_row, seat_col]

# === Part Two === /
for row in range(0, 127):
	for col in range(0, 7):
		sid = row * 8 + col
		if((sid not in seats) and ((sid-1) in seats) and ((sid+1)) in seats):
			my_seat = sid

print(f"\nPart One | Highest Seat ID: {max(seats)}")
print(f"\nPart Two | My Seat ID: {my_seat}")
