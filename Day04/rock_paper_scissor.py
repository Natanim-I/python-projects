import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: \n")
choice = int(input())
comp_choice = random.randint(0,2)
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

print("Computer choice: \n")
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

if choice == 0 and comp_choice == 2:
    print("YOU WON!!!")
elif comp_choice == 0 and choice == 2:
    print("YOU LOSE!!!")
if choice == 1 and comp_choice == 0:
    print("YOU WON!!!")
if comp_choice == 1 and choice == 0:
    print("YOU LOSE!!!")
if choice == 2 and comp_choice == 1:
    print("YOU WON!!!")
if comp_choice == 2 and choice == 1:
    print("YOU LOSE!!!")