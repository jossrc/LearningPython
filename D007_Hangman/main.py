import random
import graphics

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

win = False
end_of_game = False
lives = 6

while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()
    exists = False

    for letter in chosen_word:
        if letter == guess and letter not in display:
            exists = True
            break

    if exists:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
    else:
        lives -= 1

    print(display)
    print(graphics.stages[lives])

    if "_" not in display:
        end_of_game = True
        win = True

if win:
    print("You win")
else:
    print("You lose")
