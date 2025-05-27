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
import Game.Archive.Weapons_Menu as WeaponShop
import Game.Modules.Menu.Storage_menu as StorageShop

# Import Data Files
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

shop_menu_options = {
    1: 'Buy Pickaxes', # Pickaxe, Drill
    2: 'Buy Drills', #
    3: 'Buy Weapons', # 
    4: 'Buy Storage' # Weapons for attack/defense
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
        if planet == "Earth":
            ToolShop.tool_shop_menu("Earth", EarthData.Tools["Pickaxes"])
        elif planet == "Mars":
            ToolShop.tool_shop_menu("Mars", MarsData.Tools["Pickaxes"])
    if choice == 2:
        if planet == "Earth":
            ToolShop.tool_shop_menu("Earth", EarthData.Tools["Drills"])
        elif planet == "Mars":
            ToolShop.tool_shop_menu("Mars", MarsData.Tools["Drills"])
    if choice == 3:
        if planet == "Earth":
            ToolShop.tool_shop_menu(planet, EarthData.Tools["Weapons"])
        elif planet == "Mars":
            ToolShop.tool_shop_menu(planet, MarsData.Tools["Weapons"])
    else:
        print("Invalid choice, please try again.")
        shop_menu(planet, planet_tools, planet_weapons)

        



