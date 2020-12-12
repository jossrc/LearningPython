states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

# Positive indices
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])

# Negative indices
print(states_of_america[-1])  # Georgia
print(states_of_america[-2])  # New Jersey

# Add
states_of_america.append("Alaska")
states_of_america.extend(["New York", "Virginia", "California"])

print(states_of_america)

# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)  # [ [...], [...] ]
print(dirty_dozen[1][1])

