number = int(input("Enter a number: "))


def prime_number(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is prime number!")
    else:
        print(f"{number} is not prime number!")


prime_number(number)