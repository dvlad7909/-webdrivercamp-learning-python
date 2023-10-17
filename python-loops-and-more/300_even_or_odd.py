#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)
if random_num < 0:
    last_digit = random_num % -10
else:
    last_digit = random_num % 10
message = ""
if last_digit == 0:
    message = " is zero"
elif last_digit % 2 == 0:
    message = "is even"
else:
    message = "is odd"
print(random_num, "- the last digit", last_digit, message)
