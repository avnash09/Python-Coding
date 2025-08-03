import os, random
from coffee_machine_details import MENU, resources

money = 0

def clear_terminal():

    if os.name == "nt": #Widnows
        os.system("cls")
    else: #Mac/Linux
        os.system("clear")

clear_terminal()

def user_choice():
    while True:
        choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
        if choice in ['espresso','latte','cappuccino', 'report', 'off', 'refill']:
            return choice
        else:
            print("Invalid input! Try again.")


def print_report():
    for resource, amount in resources.items():
        if resource == "coffee":
            print(f"{resource}: {amount}g")
        else:
            print(f"{resource}: {amount}ml")
    print(f"Money: ${money}")


def is_resource_sufficiency(drink): #Here "drink" is a choice of drink which is technically a dictionary of ingredients
    """Returns True when order can be made, False if ingredients are insufficient."""

    drink_ingredients = drink["ingredients"]
    for resource, quantity in drink_ingredients.items():
        if resources[resource] < quantity:
            print(f"Sorry there is not enough {resource}")
            return False
    return True

def process_coins():
    """Returns the total caclulated from coins inserted."""
    user_coins = {}
    print("Please insert coins.")

    for coin in ["quarters","dimes", "nickles", "pennies"]:
        user_coins[coin] = int(input(f"How many {coin}? "))
    
    total = user_coins["quarters"]*0.25 + user_coins["dimes"]*0.10 + user_coins["nickles"]*0.05 + user_coins["pennies"]*0.01

    return total

def is_txn_successful(drink_cost, money_received):
    """Returns True when the payment is accepted or False if money is insufficent."""

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}🍵. Enjoy!!!")

def refill_ingredients():
    for ingredient in resources:
        refill = int(input(f"How much {"gms" if ingredient == "coffee" else "ml"} of {ingredient} do you want to replenish? "))
        resources[ingredient] += refill
    
is_on = True

while is_on:
    choice = user_choice()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print_report()
    elif choice == 'refill':
        refill_ingredients()
    else:
        drink = MENU[choice]
        if is_resource_sufficiency(drink):
            payment = process_coins()
            if is_txn_successful(drink_cost=drink['cost'], money_received=payment):
                make_coffee(drink_name=choice, order_ingredients=drink["ingredients"])


    
    
