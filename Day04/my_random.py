# We need to import random module to generate random numbers
import random

# randint(a, b) a method to generate random integer between a and b including a and b
num1 = random.randint(0, 100)
print(num1)

# random() a method to generate a floating point between 0 and 1 not including 1
num2 = random.random()
print(num2)

love_score = random.randint(0, 100)
print(f"Your love socere is {love_score}!")


# List in python
# List is a data structure that holds a group of data together and can store mixed data types
# Insertion order is maintained in list and items are accessed using indices in square brackets
my_list = ["item1", "item2", "....."]
print(my_list)
my_list[2] = "item3"
print(my_list[2])
# visit python docs for methods and functions related to list
my_list.append("....")
print((my_list))
