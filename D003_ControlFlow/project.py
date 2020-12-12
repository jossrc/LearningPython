print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

move_to = input("Do you want to go left or right? ").lower()

if move_to == "left":
  action = input("Do you want to swim or wait? ").lower()
  if action == "wait":
    door = input("Choose a door (red, blue, yellow) ").lower()
    if door == "yellow":
      print("You win!!")
    elif door == "red":
      print("Burned by fire\nGame Over!!")
    elif door == "blue":
      print("Eaten by beasts\nGame Over!!")
    else:
      print("You lose.\nGame Over!!")
  else:
    print("You were attacked by a trout\nGame Over!!")
else:  
  print("You fell into a hole.\nGame Over!!")