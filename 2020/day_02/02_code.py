#!/usr/bin/env python3

# ================================================================================
# -- File:          day_02/02_code.py
# -- Project:       advent-of-code-2020
# -- Project URL:   https://adventofcode.com/2020/
# -- Create Date:   2020-12-03 11:18
# -- Author:        moosploit
# -- Company:       https://github.com/moosploit
# -- License:       MIT License | http://www.opensource.org/licenses/MIT
# ================================================================================

import re

with open("02_data.txt") as data:
    lines = data.readlines()
    reg_pattern = "(^[0-9]+)-([0-9]+) ([a-z]{1}): ([a-z]+)"
    p1_valid_count = 0
    p2_valid_count = 0
    for line in lines:
        m = re.match(reg_pattern, line)
        min_no = int(m.group(1))
        max_no = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        char_count = password.count(char)

        # === Part One === /
        if char_count >= min_no and char_count <= max_no:
            p1_valid_count += 1

        # === Part Two === /
        if (password[min_no-1] is char and password[max_no-1] is not char) or (password[min_no-1] is not char and password[max_no-1] is char):
            p2_valid_count += 1

    print(f"Part One | Valid Lines: {p1_valid_count}")
    print(f"Part Two | Valid Lines: {p2_valid_count}")
