print("Welcome to the Tip Calculator")
total_bill = float(input("What is the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give: 12, 15, 20?\n"))
total_people = int(input("How many people to split the bill?\n"))
tip = (total_bill * (tip_percentage/100))
total = total_bill + tip
each = total / total_people
each_people = "{:.2f}".format(each)
print(f"Each people should pay: ${each_people}.")