import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
#import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Ore_Data as Ore_Data

# import controllers
import Game.Controllers.Player_Controller as Player_Controller


def smelt_ore(ore, amount, game_player):
    '''
    smelts the ore and handles inventory updates. Ore is the type,
    amount is how much ore the player has. Game_player is the player object.
    '''
    
    if ore in list((game_player.inventory["Ores"]).keys()): # list of names of ores in inventory
        if game_player.inventory["Ores"][ore]["Amount"] > 0:                         # 
            try:
                ore_data = list(Ore_Data.dict_ore_data.keys())
            except AttributeError:
                print(f"Error: {ore} data not found in Ore_Data.")
                return
        
            if ore in ore_data:

                smelting_time = Ore_Data.dict_ore_data[ore]["Smelting Time"]
                smelting_ratio = Ore_Data.dict_ore_data[ore]["Smelting Ratio"]
                smelting_yield = Ore_Data.dict_ore_data[ore]["Smelting Yield"]
                bar_name = list((smelting_yield.keys()))[0]
                bars_produced = amount//smelting_ratio
                # Update inventory
                game_player.inventory["Ores"][ore]["Amount"] -= amount
                game_player.inventory["Bars"][bar_name]["Amount"] += bars_produced

                # Print progress
                print(UtilVars.spacer)
                print(f"Smelting {amount} of {ore}...")
                print(f"Smelted {amount} of {ore} into {bars_produced} {bar_name}(s).")
                print(f"Smelting took {smelting_time} seconds.")
            else:
                print(f"{ore} data not found in ore database.")
        else:
            print(f"You don't have any of that ore.")
    else:
        print(f"{ore} is not in your inventory.")
    print(UtilVars.spacer)


def furnace_menu(game_player):
    '''
    Menu for furnace. Game_player is the player object.
    '''
    print(UtilVars.spacer)
    print(f"Welcome to the Furnace!")
    print("Which ore would you like to smelt")
    print(UtilVars.spacer)

    while True:
        for index, key in enumerate(list(game_player.inventory['Ores'].keys())):
            print(f"{index+1} | {key}")
        
        choice = (input("What option would you like to pick?: "))
        if type(choice) == str and not choice.isnumeric():
            if choice == 'back':
                break
            else:
                print('not an option')
                pass
        
        elif int(choice)-1 in range(0, len(list(game_player.inventory['Ores'].keys()))+1):
            choice = int(choice)
            selected_option = list(list(game_player.inventory['Ores'].keys()))[choice - 1]
            print(UtilVars.spacer)
            ore = selected_option
            amount = game_player.inventory['Ores'][ore]['Amount']
            smelt_ore(ore, amount, game_player)
        else:
            print('invalid')


#furnace_menu("Earth")  # Example call to the furnace menu



