# Functions can have one or more parameters
def greet_with_name(name):
    print(f"Welcome {name}!")
    print(f"How do you do {name}?")

# positional argument
greet_with_name("Natanim")


def greet_from(name, location):
    print(f"Hello {name}, How is it in {location}?")

# positional argument
greet_from("Natanim", "New York")


def square(name, number):
    print(f"Hi {name}, the square of the number you entered is {number ** 2}!")

# positional argument
square("Natanim", 4)
# keyword argument
greet_from(location="Addis Ababa", name="Natanim")