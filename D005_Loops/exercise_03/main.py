# Write your code below this row 👇

# Method 1
total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)

# Method 2
total2 = 0

for number in range(2, 101, 2):
    total2 += number

print(total2)
