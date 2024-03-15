# A Black Jack Card game implementation
import random
from black_jack_logo import logo

# List to hold the cards value
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """ A function to return a random card from the list"""
    value = random.choice(cards)
    return value


def calculate_score(cards_choices):
    """A function to take a list and return the sum of the elements"""
    if sum(cards_choices) == 21 and len(cards_choices) == 2:
        return 0
    if sum(cards_choices) > 21 and 11 in cards_choices:
        cards_choices.remove(11)
        cards_choices.append(1)
    return sum(cards_choices)


def compare(user, computer):
    """A function to compare the scores and show the result."""
    if user == computer:
        return f" Your score is {user} and Computer scored {computer}. It is a draw!"
    elif computer == 0:
        return f"Computer has a Black Jack, Computer won, You lost!"
    elif user == 0:
        return f"You have a Black Jack, You won!"
    elif user > 21:
        return f"You scored {user}. It is a Bust, You lost!"
    elif computer > 21:
        return f"Computer scored {computer}. It is a Bust, You Won"
    elif user > computer:
        return f"You scored {user}, and Computer scored {computer}. You Won!"
    else:
        return f"You scored {user}, and Computer scored {computer}. You Lost!"


def play_gmae():
    print(logo)
    # list to hold user and computer cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your  cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first choice: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to add another card or 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")
    print(compare(user_score, computer_score))
    print()


while input("Do you want play Black Jack Game, Type 'y' or 'n': ").lower() == "y":
    play_gmae()
