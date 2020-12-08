#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = 3
if number > 9:
    new = number % 10
elif number < -9:
    new = number * -1 % 10
    new = new * -1
else:
    new = number
string = "Last digit of " + str(number) + " is " + str(new)
if new > 5:
    print("{} and is greater than 5".format(string))
elif new < 6 and new != 0:
    print("{} and is less than 6 and not 0".format(string))
else:
    print("{} and is 0".format(string))
