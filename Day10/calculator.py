from calculator_art import logo


def addition(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2


def subtraction(num1, num2):
    """Subtract two numbers and return the result."""
    return num1 - num2


def multiplication(num1, num2):
    """Multiply two numbers and return the result."""
    return num1 * num2


def division(num1, num2):
    """Divide two numbers and return the result."""
    return num1 / num2


def square(num1):
    """Squares two numbers and return the result."""
    return num1 * num1


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "**": square
}


def calculator():
    """A function to control the flow of the calculation."""
    print(logo)
    num1 = float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)
    continue_calculation = True

    while continue_calculation:
        operator = input("Pick an operator: ")
        if operator != "**":
            num2 = float(input("What is the next number: "))
            result = operations[operator](num1, num2)
            print(f"{num1} {operator} {num2} = {result}")
        elif operator == "**":
            result = operations[operator](num1)
            print(f"{num1} {operator} {num1} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'new' to start a new calculation,"
                       f" or 'n' to exit: ").lower()
        if choice == "y":
            num1 = result
        elif choice == "new":
            calculator()
        elif choice == "n":
            continue_calculation = False


calculator()