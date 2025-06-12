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
    4: 'Buy Medkits',
    5: 'Buy Storage' # Weapons for attack/defense
}

def shop_menu(planet, player):#, planet_tools, planet_weapons):

    while True:
        print(f"Welcome to the {planet}'s best shop! What would you like to buy?")
        print(f"You have {player.currency} money")
        for key, option in shop_menu_options.items():
            print(f'{key} | {option}')

        choice = (input("What shop would you like to open?: "))
        print(UtilVars.spacer)
        
        if type(choice) == str and not choice.isnumeric():
            if choice == 'back':
                break
            else:
                print('Invalid Option')
        elif int(choice)-1 in range(len(list(shop_menu_options.keys()))):
            choice = int(choice)
            if choice == 1:
                if planet == "Earth":
                    ToolShop.tool_shop_menu("Earth", "Pickaxe", EarthData.Tools["Pickaxes"], player)
                elif planet == "Mars":
                    ToolShop.tool_shop_menu("Mars", "Pickaxe", MarsData.Tools["Pickaxes"], player)
            elif choice == 2:
                if planet == "Earth":
                    ToolShop.tool_shop_menu("Earth", "Drill", EarthData.Tools["Drills"], player)
                elif planet == "Mars":
                    ToolShop.tool_shop_menu("Mars", "Drill", MarsData.Tools["Drills"], player)
            elif choice == 3:
                if planet == "Earth":
                    ToolShop.tool_shop_menu(planet, "Weapons", EarthData.Tools["Weapons"], player)
                elif planet == "Mars":
                    ToolShop.tool_shop_menu(planet, "Weapons", MarsData.Tools["Weapons"], player)
            elif choice == 4:
                ToolShop.tool_shop_menu(planet, "Medi", EarthData.Tools["Medi-Tools"], player)
            elif choice == 'back':
                break
            elif choice == 'error':
                print("Invalid choice, please try again.")
        else:
            print('Invalid')
        



