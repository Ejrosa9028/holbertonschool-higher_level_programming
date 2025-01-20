#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # Esta línea ya está definida, no la toques.

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
