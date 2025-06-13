'''
this furnace menu is the wrong one, but I'll leave it here.
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Ore_Data as Ore_Data


menu_options = {
    1: 'Smelt Ore',
}

def smelt_ore(ore, amount, game_player): # game_player will be a player object, reference its inventory.
    ore_var_name = ore.replace(" ", "")
    
    if ore in game_player.inventory["Ores"]:
        if game_player.inventory["Ores"][ore]["Amount"] >= amount:
            ore_data = getattr(Ore_Data, ore_var_name)
            if ore_data:
                smelting_time = ore_data["Smelting Time"]
                smelting_ratio = ore_data["Smelting Ratio"]
                smelting_yield = ore_data["Smelting Yield"]
                bar_name = list(smelting_yield.keys())[0]
                bars_produced = amount // smelting_ratio

                game_player.inventory["Ores"][ore]["Amount"] -= amount
                game_player.inventory["Bars"][bar_name]["Amount"] += bars_produced

                print(UtilVars.spacer)
                print(f"Smelting {amount} of {ore}...")
                print(f"Smelted {amount} of {ore} into {bars_produced} {bar_name}(s).")
                print(f"Smelting took {smelting_time} seconds.")
            else:
                print(f"{ore} data not found in ore database.")
        else:
            current_amount = game_player.inventory["Ores"][ore]["Amount"]
            print(f"Not enough {ore}. You have {current_amount} but need {amount}.")
    else:
        print(f"{ore} is not in your inventory.")
    print(UtilVars.spacer)

def furnace_menu(game_player):
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
            smelt_ore(ore, amount, game_player)
        else:
            print("Invalid option.")


furnace_menu("Earth")  # Example


'''
