#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of", number, "is", end=" ")

if number < 0:
    lastdigit = (abs(number) % 10) * -1
else:
    lastdigit = number % 10
print(lastdigit, "and is", end=" ")
if lastdigit > 5:
    print("greater than 5")
elif lastdigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
