from main import MENU, resources

run = True
available_resources = resources.copy()
money = 0.0


def report():
    print(f"Water: {available_resources['water']}ml")
    print(f"Milk: {available_resources['milk']}ml")
    print(f"Coffee: {available_resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def request_payment(drink_data):
    global money
    cost = drink_data["cost"]
    print(f"This drink costs:${cost:.2f}\nPlease insert coins.\n")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if coins < cost:
        print(f"Sorry, you don't have enough money. You need ${cost:.2f}. You inserted ${coins:.2f}.")
        return False

    change = coins - cost
    money += cost
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    return True


def request_resources(drink_data):
    ingredients = drink_data["ingredients"]

    for ingredient, amount_needed in ingredients.items():
        if available_resources.get(ingredient, 0) < amount_needed:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def deduct_resources(drink_data):
    ingredients = drink_data["ingredients"]

    for ingredient, amount_needed in ingredients.items():
        available_resources[ingredient] -= amount_needed


def main():
    global run, available_resources

    request = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if request in ("espresso", "latte", "cappuccino"):
        drink_data = MENU[request]

        if request_resources(drink_data):
            if request_payment(drink_data):
                deduct_resources(drink_data)
                print(f"Here is your {request}.☕ Enjoy!")

    elif request == "report":
        report()

    elif request == "refill":
        print("Refilling...")
        available_resources = resources.copy()
        print("Resources are back to full\n")
        report()

    elif request == "exit":
        print("Thank you for playing!")
        run = False

    else:
        print("Invalid input")


while run:
    main()
