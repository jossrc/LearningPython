import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

index_name = random.randint(0, len(names) - 1)

who_pay = names[index_name]

print(f"{who_pay} is going to buy the meal today!")
