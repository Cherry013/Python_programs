from art import logo

Menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 150
}


def Check_resources(menu):
    for i in menu:
        if resources[i] < menu[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def money(cost):
    given = int(input("How many quaters?: ")) * 0.25
    given += int(input("How many dimess?: ")) * 0.1
    given += int(input("How many nickless?: ")) * 0.05
    given += int(input("How many pennies?: ")) * 0.01
    if given >= cost:
        global profit
        profit += cost
        if given == cost:
            return True
        print("Here is $%5.2f dollars in change." %(given-cost))
        return True
    else:
        return False

Machine_ON = True
print("\n"*25)
print(logo)
while Machine_ON:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    name = drink
    if drink == "off":
        Machine_ON = False
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = Menu[drink]
        res= Check_resources(drink['ingredients'])
        if res:
            suss = money(drink["cost"])
            if suss:
                #Making Coffee
                for i in drink['ingredients']:
                    resources[i] -= drink['ingredients'][i]
                print(f"Here is your {name}. Enjoy!🍵")
            else:
                print("Sorry that's not enough money. Money refunded.")

    