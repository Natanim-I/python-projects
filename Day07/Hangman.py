import random
from Hangman_words import word_list
from Hangman_ASCII import stages, logo

print(logo)
chosen_word = random.choice(word_list)
blank_char = []
chosen_word_len = len(chosen_word)
lives = 6
is_over = False

for char in range(chosen_word_len):
    blank_char += "_"

while not is_over:
    guess = input("Guess a letter: ").lower()

    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if letter == guess:
            blank_char[position] = letter
    if guess not in chosen_word:
        print(f"The letter you guessed {guess} is not in the word, You lose a life!")
        lives -= 1
        if lives <= 0:
            is_over = True
            print("You Lose!!!!")
    print(f"{' '.join(blank_char)}")

    if guess in blank_char:
        print(f"You have already guessed {guess}!")
    if "_" not in blank_char:
        is_over = True
        print("You win!!!")

    print(stages[lives])