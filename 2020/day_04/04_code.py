#!/usr/bin/env python3

# ================================================================================
# -- File:          day_04/04_code.py
# -- Project:       advent-of-code-2020
# -- Project URL:   https://adventofcode.com/2020/
# -- Create Date:   2020-12-04 10:18
# -- Author:        moosploit
# -- Company:       https://github.com/moosploit
# -- License:       MIT License | http://www.opensource.org/licenses/MIT
# ================================================================================

import re

with open("04_data.txt") as file:
    data = file.readlines()

ignore_pass_detail = "cid"


def parse_details(passport):
    passport_details = {}
    pass_details_list = passport.rstrip().split(" ")
    for detail in pass_details_list:
        pd_key, pd_value = detail.split(":")
        passport_details[pd_key] = pd_value

    return passport_details


def parse_data(data):
    passports = []
    passport_count = 0
    pass_detail_string = ""
    for i, line in enumerate(data):
        if (line != "\n"):
            pass_detail_string = pass_detail_string + line.replace("\n", " ")
            if (i == len(data) - 1):
                passport_count += 1
                passports.append(parse_details(pass_detail_string))
        else:
            passport_count += 1
            passports.append(parse_details(pass_detail_string))
            pass_detail_string = ""

    return passports


def validate_detail(detail, value):

    if detail == "byr":
        if (1920 <= int(value) <= 2002):
            return True
    elif detail == "iyr":
        if (2010 <= int(value) <= 2020):
            return True
    elif detail == "eyr":
        if (2020 <= int(value) <= 2030):
            return True
    elif detail == "hgt":
        hgt_pattern = "([0-9]{2,3})([cmin]{2}$)"
        if (re.search(hgt_pattern, value)):
            m = re.match(hgt_pattern, value)
            if ((m.group(2) == "cm") and (150 <= int(m.group(1)) <= 193)):
                return True
            if ((m.group(2) == "in") and (59 <= int(m.group(1)) <= 76)):
                return True
    elif detail == "hcl":
        hcl_pattern = "#[0-9a-f]{6}"
        if (re.search(hcl_pattern, value)):
            return True
    elif detail == "ecl":
        evv = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if (value in evv):
            return True
    elif detail == "pid":
        pid_pattern = "^[0-9]{9}$"
        if (re.search(pid_pattern, value)):
            return True


def check_passport(passport):
    valid_details = 0

    if validate_detail("byr", passport['byr']):
        valid_details += 1
    if validate_detail("iyr", passport['iyr']):
        valid_details += 1
    if validate_detail("eyr", passport['eyr']):
        valid_details += 1
    if validate_detail("hgt", passport['hgt']):
        valid_details += 1
    if validate_detail("hcl", passport['hcl']):
        valid_details += 1
    if validate_detail("ecl", passport['ecl']):
        valid_details += 1
    if validate_detail("pid", passport['pid']):
        valid_details += 1

    if valid_details == 7:
        return True


def part_one():
    valid_passports = 0
    for passport in parse_data(data):
        amount_pass_details = len(passport)
        if (amount_pass_details == 8) or ((amount_pass_details == 7) and ignore_pass_detail not in passport):
            valid_passports += 1
    return valid_passports


def part_two():
    valid_passports = 0
    for passport in parse_data(data):
        amount_pass_details = len(passport)
        if ((amount_pass_details == 8) or ((amount_pass_details == 7) and (ignore_pass_detail not in passport))):
            if check_passport(passport):
                valid_passports += 1
    return valid_passports


print(f"\nPart One | Valid Passports: {part_one()}")
print(f"\nPart Two | Valid Passports: {part_two()}")
