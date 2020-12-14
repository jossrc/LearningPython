fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print(fruits)

# For Loop with Range

for number in range(1, 10):  # [1;10>
    print(number)

for number in range(1, 10, 3):  # + 3
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)
