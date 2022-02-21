from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from Money_machine import MoneyMachine





menu=Menu()

money_machine=MoneyMachine()
# drink=menuitem.ingredients
coffee_maker=CoffeeMaker()






off=False
while off==False:
    options=menu.get_items()
    guess=input(f"What would you like {options}:")
    if guess=="off":
        off=True

    elif guess=="report":
        coffee_maker.report()
        money_machine.report()
        off=False
    else:
        drink=menu.find_drink(guess)
        # print(drink)
        b=coffee_maker.is_resource_sufficient(drink)
        if b :

            print("yee")
            check=money_machine.make_payment(drink.cost)
            if check ==True:
                coffee_maker.make_coffee(drink)


        else:
            print("not enough resources")
            off=False




