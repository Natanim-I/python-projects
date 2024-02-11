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

game_images = [rock, paper, scissors]
print("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: \n")
choice = int(input())
comp_choice = random.randint(0,2)
if choice > 2 or choice < 0:
    print("WRONG INPUT!!!")
    print("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: \n")
    choice = int(input())
else:
    print(game_images[choice])
    print("Computer choice: \n")
    print(game_images[comp_choice])
    if choice == 0 and comp_choice == 2:
        print("YOU WON!!!")
    elif comp_choice == 0 and choice == 2:
        print("YOU LOSE!!!")
    elif comp_choice > choice == 2:
        print("YOU LOSE!!!")
    elif choice > comp_choice:
        print("YOU WON!!!")
    elif comp_choice == choice:
        print("DRAW!!!")
