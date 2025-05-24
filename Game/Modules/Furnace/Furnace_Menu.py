import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Ore_Data as OreData


menu_options = {
    1: 'Smelt Ore',
}
def furnace_menu(Planet):
    print(UtilVars.spacer)
    print(f"Welcome to the {Planet} Furnace!")
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
            smelt_ore(ore, amount)
        else:
            print("Invalid option.")


furnace_menu("Earth")  # Example call to the furnace menu

def smelt_ore(ore, amount):
    print(f"Smelting {amount} of {ore}...")
    if ore in Player.Data["Inventory"]["Ores"]:
        if Player.Data["Inventory"]["Ores"][ore]["Amount"] >= amount:
            Player.Data["Inventory"]["Ores"]["Amount"] -= amount
            print(f"Smelting {amount} of {ore}...")
            if ore in OreData.Ore_Data:
                smelting_time = OreData.Ore_Data[ore]["Smelting Time"]
                smelting_ratio = OreData.Ore_Data[ore]["Smelting Ratio"]
                smelting_yield = OreData.Ore_Data[ore]["Smelting Yield"]
                Player.Data["Inventory"]["Bars"][smelting_yield] += amount / smelting_ratio
                print(f"Smelted {amount} of {ore} into {smelting_yield}.")
            else:
                print(f"{ore} is not a valid ore.")
        else:
            print(f"You do not have enough {ore} to smelt.")
    else:
        print(f"{ore} is not in your inventory.")
    print(UtilVars.spacer)

