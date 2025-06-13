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

    
def tool_shop_menu(Planet, Menu, items, player):
    '''
    Handles the buying of tools. Planet is the name of the planet,
    Menu is the name of the menu, items is a dictionary of items available for purchase,
    and player is the player object.
    '''
    print(f"Welcome to the {Planet} {Menu} Shop!")
    print("Here are the available tools:")
    print(UtilVars.spacer) 

    # Display available tools
    for index, tool in enumerate(items.keys(), 1):
        print(f"{index} | {tool}")
    print(UtilVars.spacer)
    
    try:
        choice = int(input("Select a tool (1-" + str(len(items)) + "): "))
        if choice in range(1, len(items) + 1):
            selected_tool = list(items.keys())[choice - 1]
            tool_data = items[selected_tool]
            
            # Display tool details
            print(UtilVars.spacer)
            print(f"Available {selected_tool}:")
            print(f"- Price: {tool_data['Buy Price']}")
            print(f"- Description: {tool_data['Description']}")
            print(UtilVars.spacer)
            
            confirm = input("Would you like to buy this tool? (y/n): ").lower()
            if confirm == 'y':
                purchase_tool(selected_tool, tool_data['Buy Price'], player)
            else:
                print("Purchase cancelled.")
        else:
            print("Invalid tool selection.")
    except ValueError:
        print("Please enter a valid number.")


def purchase_tool(tool, price, player):

    '''
    if Player.Data["Currency"]>= price:
        PlayerController.currency_controller("remove", price)
        PlayerController.inventory_controller("add", tool, player)
        print(f"You have purchased {tool} for {price} money. You now have {Player.Data['Currency']} left.")
        
    elif Player.Data["Currency"] < price:
        print("You do not have enough money to purchase this tool.")
        print(f"You need {price - Player.Data['Currency']} more money.")
    '''

    if player.currency >= price:
        PlayerController.currency_controller("remove", price, player)
        PlayerController.inventory_controller("add", tool, player)

        if tool in list(EarthData.Tools["Medi-Tools"].keys()) or tool \
            in list(MarsData.Tools["Medi-Tools"].keys()):
            if player.health<100:
                if tool == "Medkit":
                    player.health+=20

                    if player.health>100:
                        player.health=100
                    print(f"Your health is now {player.health}")
                elif tool == "Bandage":
                    player.health+=10

                    if player.health>100:
                        player.health=100
                    print(f"Your health is now {player.health}")
            else:
                print("Your health is already full.")
                PlayerController.currency_controller("add", price, player)
        else:
            print(f"You have purchased {tool} for {price} money."
                 +f" You now have {player.currency} left.")
    elif player.currency < price:
        print("You do not have enough money to purchase this tool.")
        print(f"You need {price - player.currency} more money.")
#------------------------------------------------------------------------------