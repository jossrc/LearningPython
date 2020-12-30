import random

random_number = random.randint(1, 100)

# GUESS THE NUMBER

attempts = {
    "easy": 10,
    "hard": 5
}

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts_remaining = attempts[difficulty]

while attempts_remaining > 0:
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    number = int(input("Make a guess: "))
    if number < random_number:
        print("Too low.")
    elif number > random_number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {random_number}")
        break

    attempts_remaining -= 1

    if attempts_remaining == 0:
        print("You've run out of guesses, you lose")
