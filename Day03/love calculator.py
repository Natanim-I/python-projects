print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

first_digit = 0
second_digit = 0
name = name1 + " " + name2
first_digit = name.lower().count('t')
first_digit += name.lower().count('r')
first_digit += name.lower().count('u')
first_digit += name.lower().count('e')
second_digit = name.lower().count('l')
second_digit += name.lower().count('o')
second_digit += name.lower().count('v')
second_digit += name.lower().count('e')
love_percent = int(str(first_digit) + str(second_digit))

if love_percent < 10 or love_percent > 90:
  print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent >= 40 and love_percent <= 50:
  print(f"Your score is {love_percent}, you are alright together.")
else:
  print(f"Your score is {love_percent}.")


