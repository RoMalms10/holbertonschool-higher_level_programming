#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    roman_sum = 0
    for numer in roman_string:
        if numer in my_dict:
            roman_sum += my_dict[numer]
        else:
            return 0
    for check in range(len(roman_string) - 1):
        if my_dict[roman_string[check]] < my_dict[roman_string[check + 1]]:
            roman_sum -= my_dict[roman_string[check]] * 2
            check += 1
    return roman_sum
