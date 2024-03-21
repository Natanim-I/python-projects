import math
from logo import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def generate_report():
    """A function to generate a printable report of the resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_coins(quarters=0, dimes=0, nickles=0, pennies=0):
    """A function to process the coins and return the total money in dollar."""
    total = ((quarters/4) + (dimes/10) + (nickles/20) + (pennies/100))
    return float("{:.2f}".format(total))


def check_amount(order):
    """A function to check the sufficiency of the ingredients in resource."""
    for item in MENU[order]['ingredients']:
        if resources[item] < MENU[order]['ingredients'][item]:
            return item
    return True


def process_payment(order, total_money):
    """A function to charge the money and return the change."""
    global profit
    if total_money > MENU[order]['cost']:
        change = total_money - MENU[order]['cost']
        profit += MENU[order]['cost']
        return float("{:.2f}".format(change))
    else:
        return 0


def process_order(order):
    """A function to make the coffee and decrease the resource."""
    for item in MENU[order]['ingredients']:
        resources[item] -= MENU[order]['ingredients'][item]
    return order


customer_choice = ""
money = 0

print(logo)
while customer_choice != 'off':
    customer_choice = input("What would you like (espresso/latte/cappuccino): ").lower()
    if customer_choice == 'espresso' or customer_choice == 'latte' or customer_choice == 'cappuccino':
        amount = check_amount(customer_choice)
        if amount == True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money += process_coins(quarters, dimes, nickles, pennies)
            print(f"Your total money is ${money}")
            money = process_payment(customer_choice, money)
            if money == 0:
                print("Sorry, you dont have enough money.")
            else:
                print(f"Here is ${money} in change.")
                order = process_order(customer_choice)
                print(f"Here is your {order} ☕, Enjoy!")
        else:
            print(f"Sorry there is no enough {amount}!")
    elif customer_choice == 'report':
        generate_report()
    elif customer_choice == 'off':
        print("Thank you, Enjoy your coffee!")
    else:
        print("Wrong Input, Try Again!")