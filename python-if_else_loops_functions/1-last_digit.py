#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # Esta línea ya está definida, no la toques.
last_digit = abs(number) % 10  # Obtenemos el último dígito

# Si el número es negativo, ajustamos el último dígito para reflejar el signo
if number < 0:
    last_digit = -last_digit

print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
