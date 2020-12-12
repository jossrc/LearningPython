import random
import graphics_project

# Rock Paper Scissors Game

graphics = [graphics_project.rock, graphics_project.paper, graphics_project.scissors]
choice = int(input("What do you choose? Type 0 for Rock ✊🏻, 1 for Paper ✋🏻 or 2 for Scissors ✌🏻.\n"))
computer = random.randint(0, 2)

print("")
print(graphics[choice] + "\n")
print("Computer chose:\n")
print(graphics[computer] + "\n")

if (choice == 1 and computer == 0) or (choice == 2 and computer == 1) or (choice == 0 and computer == 2):
    print("You win")
elif (choice == 0 and computer == 1) or (choice == 1 and computer == 2) or (choice == 2 and computer == 0):
    print("You lose")
else:
    print("Draw")
