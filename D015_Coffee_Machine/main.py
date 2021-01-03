import data

money = 0
is_on = True


def check_resources(drink_ingredients: dict[str, float]) -> bool:
    for item, value in drink_ingredients.items():
        if value > data.resources[item]:
            print(f"Sorry there is not enough {value}")
            return False
    return True


def process_coins():
    # TODO
    print("Please insert coins.")


choice = input("What would you like? (espresso/ latte/ cappuccino): ")

if choice == "off":
    is_on = False
elif choice == "report":
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: {money}")
else:
    drink = data.MENU[choice]
    are_there_enough_resources = check_resources(drink["ingredients"])
    if are_there_enough_resources:
        process_coins()

