# print() function related
# display Hello World String to console
print("Hello World")
# display Hello World on separate lines using the \n character
print("Hello World\nHello World\nHello World")
# display Hello World concatinated to my name
print("Hello World, " + "Natanim Eibrahim")

# input() function related
# prompt a user for name and accept value
input("What is your name : ")
# greet a custome by taking thie name
print("Hello " + input("What is your name: "))

# variables
# store my name to variable called name
name = "Abebe"
print(name)
# updating the value of name
name = "Natanim"
print(name)
name = input("What is your name: ")
# casting to string using the str() function
length = str(len(name))
print("There are " + length + " characters in your name!")

# Day 1 project
# Band name generator
print("Welcome to our Band name generator :)")
city_name = input("What is the name of the city you were born in? \n")
pet_name = input("What is the name of your pet? \n")
band_name = pet_name + " " + city_name
print("Your band name could be: " + band_name)

