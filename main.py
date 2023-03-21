
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coins():
    print('Please insert coins.')
    quarters = int(input('how many quarters?:'))
    dimes = int(input('how many dimes?:'))
    nickles = int(input('how many nickles?:'))
    pennies=int(input('how many pennies?:'))
    sum = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return sum


def report(resources,money):
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')


def check_suffic(coffee,resource):
    if resource["water"]<coffee['water']:
        print(f'Sorry there is not enough water.')
        return False
    elif resource["milk"] < coffee.get('milk',0):
            print(f'Sorry there is not enough milk.')
            return False

    elif resource["coffee"]<coffee['coffee']:
        print(f'Sorry there is not enough coffee.')
        return False
    return True


print(resources)

money_resource = 0
flag = True

while flag:
    answer = input(' What would you like? (espresso/latte/cappuccino):')
    while answer!='off':

        if answer == 'report':
            report(resources,money_resource)
        elif answer == 'off':
            flag = False
        else:
            rs = check_suffic(MENU[answer]['ingredients'], resources)
            if rs:
                insertes_money = coins()
                print(insertes_money)
                if insertes_money >= MENU[answer]['cost']:
                    resources["water"] = resources["water"] - MENU[answer]['ingredients']['water']
                    if MENU[answer]['ingredients'].get("milk", 0):
                        resources["milk"] = resources["milk"] - MENU[answer]['ingredients']['milk']
                    resources["coffee"] = resources["coffee"] - MENU[answer]['ingredients']['coffee']
                    money_resource += MENU[answer]['cost']
                    change = round(insertes_money - MENU[answer]['cost'],2)
                    print(f"Here's your change ${change}")
                    print(f"Here is your {answer} ☕. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                flag=False
        answer = input(' What would you like? (espresso/latte/cappuccino):')






