from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Hello, welcome to the Coffee Machine!")

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
exit = False

while not exit:
    user_input = input("\nWhat can I do for you? (report/items/*item name*/exit\n").lower()

    if user_input == 'report':
        coffee_maker.report()
    elif user_input == 'items':
        print(menu.get_items())
    elif user_input == 'exit':
        print("kthxbye")
        exit = True
    else:
        chosen_item = menu.find_drink(user_input)
        if chosen_item is not None:
            if coffee_maker.is_resource_sufficient(chosen_item):
                money_machine.report()
                
                # Ask for payment
                if money_machine.make_payment(chosen_item.cost):
                    # Make coffee if payment succesfull
                    coffee_maker.make_coffee(chosen_item)

                money_machine.report()
