my_dictionary = {
    "Key": "I am the value",
    "Key2": "Other value"
}

print(my_dictionary)
print(my_dictionary["Key"])

# Adding new items to dictionary
my_dictionary["Key3"] = "Value 3"

# Create an empty dictionary.
empty_dictionary = {}

# Edit an item in a dictionary
my_dictionary["Key"] = "I am a bug"
print(my_dictionary["Key"])

# Loop through a dictionary
for thing in my_dictionary:
    print(thing)  # keys

# Iterating over dictionaries using 'for' loops
for key, value in my_dictionary.items():
    print(key, value)

# Wipe an existing dictionary
my_dictionary = {}
print(my_dictionary)


