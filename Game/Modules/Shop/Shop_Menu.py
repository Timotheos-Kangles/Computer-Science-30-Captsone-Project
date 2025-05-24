import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import Shop Modules
import Game.Modules.Shop.Tools_Menu as ToolShop
import Game.Modules.Shop.Weapons_Menu as WeaponShop

# Import Data Files
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

shop_menu_options = {
    1: 'Buy tools', # Pickaxe, Drill
    2: 'Buy storage', # 
    3: 'Buy weapons' # Weapons for attack/defense
}

def shop_menu(planet, planet_tools, planet_weapons):
    print(f"Welcome to the {planet}'s best shop!")
    for key, option in shop_menu_options.items():
        print(f'{key} | {option}')
    try:
        choice = int(input("What shop would you like to open?: "))
        print(UtilVars.spacer)
    except:
        print("error")
    if choice == 1:
       ToolShop.tool_shop_menu(planet, planet_tools)
    if choice == 2:
        pass
    if choice == 3:
        WeaponShop.tool_shop_menu(planet, planet_weapons)



