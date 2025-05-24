# Import Others
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

# Import Controllers
import Game.Controllers.Player_Controller as PlayerController
    
def tool_shop_menu(Planet, weapons):
    print(f"Welcome to the {Planet} Weapon Shop!")
    print("Here are the available Weapons!:")
    print(UtilVars.spacer) 

    for index, category in enumerate(weapons.keys(), 1):
        print(f"{index} | {category}")
    print(UtilVars.spacer)
    choice = int(input("Please select a category (1, 2, 3): "))
    
    if choice in range(1, len(weapons) + 1):
        selected_category = list(weapons.keys())[choice - 1]
        print(f"\nAvailable {selected_category}:")
        for index, weapon in enumerate(weapons[selected_category].keys(), 1):
            print(f"{index} | {weapon}")
        
        weapon_choice = int(input("Select a weapon to purchase: "))
        if weapon_choice in range(1, len(weapons[selected_category]) + 1):
            selected_weapon = list(weapons[selected_category].keys())[weapon_choice - 1]
            weapon_data = weapons[selected_category][selected_weapon]
            print(UtilVars.spacer)
            print(f"Price: {weapon_data['Buy Price']}")
            print(f"Description: {weapon_data['Description']}")
            confirm = input("Would you like to buy this tool? (y/n): ").lower()
            if confirm == 'y':
                purchase_tool(selected_weapon, weapon_data['Buy Price'])
            else:
                print("Purchase cancelled.")
        else:
            print("Invalid tool selection.")
    else:
        print("Invalid category selection.")


def purchase_tool(tool, price):
    if Player.Data["Currency"]>= price:
        PlayerController.currency_controller("remove", price)
        PlayerController.inventory_controller("add", tool)
        print(f"You have purchased {tool} for {price} money. You now have {Player.Data['Currency']} left.")
        
    elif Player.Data["Currency"] < price:
        print("You do not have enough money to purchase this tool.")
        print(f"You need {price - Player.Data['Currency']} more money.")

