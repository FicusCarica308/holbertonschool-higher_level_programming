#!/usr/bin/python3
count = 2
for i in range(122, 96, -1):
    if count % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
    count = count + 1
print()
