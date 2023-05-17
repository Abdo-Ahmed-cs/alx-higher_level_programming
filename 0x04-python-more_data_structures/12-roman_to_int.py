#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for index in range(0, len(roman_string)):
        if index < len(roman_string) - 1:
            letter1 = roman_string[index]
            letter2 = roman_string[index + 1]
            if letter1 in 'I' and letter2 in 'VX':
                result -= romans.get(roman_string[index])
            elif letter1 in 'X' and letter2 in 'CL':
                result -= romans.get(roman_string[index])
            elif letter1 in 'C' and letter2 in 'DM':
                result -= romans.get(roman_string[index])
            else:
                result += romans.get(roman_string[index])
        else:
            result += romans.get(roman_string[index])
    return result
