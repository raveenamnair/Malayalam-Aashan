""" This file will contain data structures and constants that have the unicode values for each alphabet category
    https://www.win.tue.nl/~aeb/natlang/malayalam/malayalam-alphabet.html
"""

UNICODE_STARTING_VALUE = 0x0D00
UNICODE_ENDING_VALUE = 0x0D7F

# 0x0D29 is a value that doesn't exist
# [starting - ending]
CONSONANT_RANGE = [0x0D15, 0x0D39]

# Modifying consonant symbols have a broken range
# first 6 are written to the right of corresponding consonant
# next 3 are written to the left of corresponding consonant
# last 3 are written to the right of corresponding consonant
MODIFY_CONSONANT_RANGE = [[0x0D3E, 0x0D43], [0x0D46, 0x0D48], [0x0D4A, 0x0D4D], [0x0D02, 0x0D03]]

# 0x0D0D and 0x0D11
INDEPENDENT_VOWEL_RANGE = [[0x0D05, 0x0D14], [0x0D60, 0x0D61]]

# Values that are not defined yet in unicode table
IGNORE_VALUES = [0x0D29, 0x0D0D, 0x0D11]


def get_vowels():
    vowels = []
    for index in INDEPENDENT_VOWEL_RANGE:
        start = index[0]
        end = index[1]
        for i in range(start, (end + 1)):
            if i not in IGNORE_VALUES:
                vowels.append(chr(i))

    return vowels


def get_consonants():
    consonants = []
    start = CONSONANT_RANGE[0]
    end = CONSONANT_RANGE[1]
    for x in range(start, end+1):
        consonants.append(chr(x))
    return consonants


def get_modify_vowels():
    modify = []
    for index in MODIFY_CONSONANT_RANGE:
        start = index[0]
        end = index[1]
        for i in range(start, (end + 1)):
            if i not in IGNORE_VALUES:
                modify.append(chr(i))
    return modify