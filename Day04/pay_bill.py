import random

names = input("Enter the names separated by a comma: \n").split(", ")

last_index = len(names) - 1
random = random.randint(0, last_index)

print(f"{names[random]} is going to buy the meal today!!!")
