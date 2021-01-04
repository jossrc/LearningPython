import data

money = 0.0
is_on = True


def check_resources(drink_ingredients: dict[str, float]) -> bool:
    for item, value in drink_ingredients.items():
        if value > data.resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    amount_to_coins = int(input("How many quarters?: "))*0.25
    amount_to_coins += int(input("Hoy many dimes?: "))*0.10
    amount_to_coins += int(input("Hoy many nickles?: "))*0.05
    amount_to_coins += int(input("Hoy many pennies?: "))*0.01
    return amount_to_coins


def is_transaction_successful(money_received:float , cost_of_drink:float):
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change")
        global money
        money += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name: str, ingredients_for_the_drink: dict[str, float]):
    for ingredient in ingredients_for_the_drink:
        data.resources[ingredient] -= ingredients_for_the_drink[ingredient]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/ latte/ cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = data.MENU[choice]
        are_there_enough_resources = check_resources(drink["ingredients"])
        if are_there_enough_resources:
            amount_to_pay = process_coins()
            is_there_enough_money = is_transaction_successful(amount_to_pay, drink["cost"])
            if is_there_enough_money:
                make_coffee(choice, drink["ingredients"])
