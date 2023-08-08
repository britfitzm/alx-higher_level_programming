#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	return "number is positive"
elif number < 0:
	return "number is negative"
elif number == 0:
	return "number is zero"
else:
	return "error"
