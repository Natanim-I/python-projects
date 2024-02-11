target = int(input("Enter a number between 1 and 1000: \n"))

# We can implement the sum of even numbers between 0 and 100 in two ways
# Using the for loop and modulo operator
sum = 0
for num in range(0, target + 1):
    if num % 2 == 0:
        sum += num
print(sum)

#Using the for loop and the range function steps argument
sum = 0
for num in range(0, target + 1, 2):
    sum += num
print(sum)