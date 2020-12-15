import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

guess = input("Guess a letter: ").lower()
exists = False

for letter in chosen_word:
    if letter == guess:
        exists = True
        break

if exists:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
else:
    print("Wrong !!")

print(display)
