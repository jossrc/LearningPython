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
