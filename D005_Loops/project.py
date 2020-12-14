# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for nr in range(1, nr_letters + 1):
    random_position = random.randint(1, len(letters) - 1)
    password.append(letters[random_position])

for nr in range(1, nr_symbols + 1):
    random_position = random.randint(1, len(symbols) - 1)
    password.append(symbols[random_position])

for nr in range(1, nr_numbers + 1):
    random_position = random.randint(1, len(numbers) - 1)
    password.append(numbers[random_position])

aux = ""

for position in range(1, len(password)):
    random_position = random.randint(1, len(password) - 1)
    aux = password[position]
    password[position] = password[random_position]
    password[random_position] = aux

print("".join(password))
