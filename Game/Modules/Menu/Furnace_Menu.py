import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
#import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Ore_Data as OreData

# import controllers
import Game.Controllers.Player_Controller as Player_Controller

menu_options = {
    1: 'Smelt Ore',
}

def smelt_ore(ore, amount, game_player):
    # Remove space and combine words for matching OreData variable names
    ore_var_name = ore.replace(" ", "")
    Player = Player_Controller.fetch_player_data(game_player)
    if ore in Player.Data["Inventory"]["Ores"]:
        if Player.Data["Inventory"]["Ores"][ore]["Amount"] >= amount:
            ore_data = getattr(OreData, ore_var_name)
            if ore_data:
                smelting_time = ore_data["Smelting Time"]
                smelting_ratio = ore_data["Smelting Ratio"]
                smelting_yield = ore_data["Smelting Yield"]
                bar_name = list(smelting_yield.keys())[0]
                bars_produced = amount // smelting_ratio

                # Update inventory
                Player.Data["Inventory"]["Ores"][ore]["Amount"] -= amount
                Player.Data["Inventory"]["Bars"][bar_name]["Amount"] += bars_produced

                # Print progress
                print(UtilVars.spacer)
                print(f"Smelting {amount} of {ore}...")
                print(f"Smelted {amount} of {ore} into {bars_produced} {bar_name}(s).")
                print(f"Smelting took {smelting_time} seconds.")
            else:
                print(f"{ore} data not found in ore database.")
        else:
            current_amount = Player.Data["Inventory"]["Ores"][ore]["Amount"]
            print(f"Not enough {ore}. You have {current_amount} but need {amount}.")
    else:
        print(f"{ore} is not in your inventory.")
    print(UtilVars.spacer)

def furnace_menu(Player):
    print(UtilVars.spacer)
    print(f"Welcome to the Furnace!")
    print("Here are the available Options:")
    print(UtilVars.spacer)

    for key, option in menu_options.items():
        print(f'{key} | {option}')
    print(UtilVars.spacer)
    
    choice = int(input("What option would you like to pick?: "))
    if choice in range(1, len(menu_options) + 1):
        selected_option = list(menu_options.keys())[choice - 1]
        if selected_option == 1:
            print(UtilVars.spacer)
            ore = input("Enter the ore you want to smelt: ")
            amount = int(input("Enter the amount of ore you want to smelt: "))
            smelt_ore(ore, amount, Player)
        else:
            print("Invalid option.")


#furnace_menu("Earth")  # Example call to the furnace menu



