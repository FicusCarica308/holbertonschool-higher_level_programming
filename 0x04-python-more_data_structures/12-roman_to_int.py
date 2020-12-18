#!/usr/bin/python3
def roman_to_int(roman_string):
    final = 0
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    numerals = {'MMM': 3000, 'MM': 2000, 'CM': 900, 'DCCC': 800,
                'DCC': 700, 'DC': 600, 'CD': 400, 'CCC': 300,
                'CC': 200, 'XC': 90, 'LXXX': 80, 'LXX': 70,
                'LX': 60,  'XL': 40, 'XXX': 30, 'XX': 20,
                'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6, 'IV': 4,
                'III': 3, 'II': 2, 'I': 1
                }
    roman = {'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    cool = sorted(numerals.items(), key=lambda item: item[1], reverse=True)
    for key in cool:
        if key[0] in roman_string:
            roman_string = roman_string.replace(key[0], "")
            final += numerals.get(key[0])
    if len(roman_string) == 1:
        for key in roman:
            if key in roman_string:
                final += roman.get(key)
    return final
