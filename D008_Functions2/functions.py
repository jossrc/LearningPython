def greet():
    print("Hello")
    print("How are you?")
    print("Welcome")


greet()


# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Joss")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# Positional Argument
greet_with("Jack Bauer", "Nowhere")

# Keyword Arguments
greet_with(location="Lima", name="Jose Robles")
