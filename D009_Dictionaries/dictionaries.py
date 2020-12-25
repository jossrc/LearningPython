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

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# Nesting Dictionary in a List

travel_log_arr = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
