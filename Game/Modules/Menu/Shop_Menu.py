import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import Menu Modules
import Game.Modules.Menu.Tools_Menu as ToolShop
import Game.Modules.Menu.Weapons_Menu as WeaponShop

# Import Data Files
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

shop_menu_options = {
    1: 'Buy Tools', # Pickaxe, Drill
    2: 'Buy Weapons', # 
    3: 'Buy Storage' # Weapons for attack/defense
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
        WeaponShop.tool_shop_menu(planet, planet_weapons)
    if choice == 3:
        pass


