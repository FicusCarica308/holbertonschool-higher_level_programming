#!/usr/bin/python3
def print_last_digit(number):
    if number > 9:
        number = number % 10
        print(number, end="")
        return number
    elif number < -9:
        number = number * -1 % 10
        print(number, end="")
        return number
    else:
        print(number, end="")
        return number
