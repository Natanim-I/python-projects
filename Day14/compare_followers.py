# A game to compare the number of instagram followers
import random
from art_logo import logo, vs
from game_data import data


# Generating a random account from the data
def random_person():
    """A function to pick a random account from the list of data provided."""
    person = random.choice(data)
    return person


# creating two variables to hold the random accounts
first_account = random_person()
second_account = random_person()
# comparing and regenerating the second account if the accounts are equal
if first_account == second_account:
    second_account = random_person()


def format_data(account):
    """Formats the account data into printable format."""
    return f"{account['name']}, {account['description']} from {account['country']}."


# Comparing the two accounts based on their follower number
def compare(person1, person2):
    """A function to compare the number of followers of the accounts."""
    if person1['follower_count'] > person2['follower_count']:
        return person1
    elif person2['follower_count'] > person1['follower_count']:
        return person2
    else:
        return 0


score = 0
user_choice = ""
is_game_over = False

print(logo)

while not is_game_over:
    print()
    print(f"Compare A: {format_data(first_account)}")
    print(vs)
    print(f"Against B: {format_data(second_account)}")
    print()

    choice = input("Who has more followers, Type 'A' or 'B': ").upper()
    if choice == 'A':
        user_choice = first_account
    elif choice == 'B':
        user_choice = second_account
    result = compare(first_account, second_account)
    if user_choice == result:
        first_account = user_choice
        second_account = random_person()
        score += 1
        print(f"You are right, Current score {score}")
    else:
        print(f"Sorry that is wrong, final score {score}")
        is_game_over = True
