from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(start_text, shift_amount, shift_direction):
    end_text = ""
    if shift_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {shift_direction}d text is: {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type your shift amount: \n"))
    shift %= 26
    caesar(start_text=text, shift_amount=shift, shift_direction=direction)
    result = input("Type 'yes' to go again. Otherwise, type 'no': \n").lower()
    if result == "no":
        should_continue = False
        print("Thankyou for using Caesar Cipher!!!")




