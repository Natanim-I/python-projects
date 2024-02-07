# Mathematical operations and F-string in python
# Matehmatical operations are always performed in PEMDASLR-(Parenthesis Exponential Multiplication Division AAddition Subtraction Left to Right)
num1 = 123_45
num2 = 567
# Addition using the + operator
sum = num1 + num2
print(sum)
# Subtraction using the - operator
difference = num1 - num2
print(difference)
# Multiplication using the * operator
product = num1 * num2
print(product)
# Division using the / operator returns a float number always
quotient = num1 / num2
print(quotient)
# Division using the // operator returns an integer always
quotient = num1 // num2
print(quotient)
# Exponential using the ** operator
power = num2 ** 2
print(power)
# Remainder using the % operator
remainder = num1 % num2
print(remainder)

# F-string
print(f"Player 1 score is {num1} and player 2 only scored {num2}. So player one won the game with {difference} difference!!!")