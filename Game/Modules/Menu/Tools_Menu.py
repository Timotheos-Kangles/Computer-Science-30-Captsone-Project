import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Others
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

# Import Controllers
import Game.Controllers.Player_Controller as PlayerController


#  python -m Game.Modules.Shop.Tools_Menu 
# TEST

    
def tool_shop_menu(Planet, items):
    print(f"Welcome to the {Planet} Tool Shop!")
    print("Here are the available tools:")
    print(UtilVars.spacer) 

    for index, category in enumerate(items.keys(), 1):
        print(f"{index} | {category}")
    print(UtilVars.spacer)
    choice = int(input("Please select a category (1, 2, 3): "))
    
    if choice in range(1, len(items) + 1):
        selected_category = list(items.keys())[choice - 1]
        print(f"\nAvailable {selected_category}:")
        for index, item in enumerate(items[selected_category].keys(), 1):
            print(f"{index} | {item}")
        
        tool_choice = int(input("Select a tool: "))
        if tool_choice in range(1, len(items[selected_category]) + 1):
            selected_tool = list(items[selected_category].keys())[tool_choice - 1]
            tool_data = items[selected_category][selected_tool]
            print(UtilVars.spacer)
            print(f"Price: {tool_data['Buy Price']}")
            print(f"Description: {tool_data['Description']}")
            confirm = input("Would you like to buy this tool? (y/n): ").lower()
            if confirm == 'y':
                purchase_tool(selected_tool, tool_data['Buy Price'])
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

