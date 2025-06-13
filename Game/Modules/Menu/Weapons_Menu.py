import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Others
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import Controllers
import Game.Controllers.Player_Controller as PlayerController


def weapon_shop_menu(Planet, items):
    '''
    Handles the buying of weapons. Planet is the name of the planet,
    items is a dictionary of items available for purchase.
    '''
    print(f"Welcome to the {Planet} Weapons Shop!")
    print("Here are the available weapons:")
    print(UtilVars.spacer) 

    # Display available weapons
    for index, weapon in enumerate(items.keys(), 1):
        print(f"{index} | {weapon}")
    print(UtilVars.spacer)
    
    try:
        choice = int(input("Select a weapon (1-" + str(len(items)) + "): "))
        if choice in range(1, len(items) + 1):
            selected_weapon = list(items.keys())[choice - 1]
            weapon_data = items[selected_weapon]
            
            # Display weapon details
            print(UtilVars.spacer)
            print(f"Available {selected_weapon}:")
            print(f"- Price: {weapon_data['Buy Price']}")
            print(f"- Description: {weapon_data['Description']}")
            print(UtilVars.spacer)
            
            confirm = input("Would you like to buy this weapon? (y/n): ").lower()
            if confirm == 'y':
                purchase_weapon(selected_weapon, weapon_data['Buy Price'])
            else:
                print("Purchase cancelled.")
        else:
            print("Invalid weapon selection.")
    except ValueError:
        print("Please enter a valid number.")

def purchase_weapon(weapon, price):
    if Player.Data["Currency"] >= price:
        PlayerController.currency_controller("remove", price)
        PlayerController.inventory_controller("add", weapon)
        print(f"You have purchased {weapon} for {price} money. You now have {Player.Data['Currency']} left.")
    else:
        print("You do not have enough money to purchase this weapon.")
        print(f"You need {price - Player.Data['Currency']} more money.")

