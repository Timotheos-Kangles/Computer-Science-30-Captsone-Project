
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))


# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

# Import Menu Modules
import Game.Modules.Menu.Shop_Menu as ShopMenu
import Game.Modules.Menu.Furnace_Menu as FurnaceMenu
import Game.Modules.Menu.Planet_Selection_menu as PlanetSelectMenu

def fetch_menu(Menu):
    if Menu == "Furnace":
        FurnaceMenu.furnace_menu()
    elif Menu == "Shop":
        ShopMenu.shop_menu("Earth", EarthData.Tools, EarthData.Tools["Weapons"])
    elif Menu == "Planet Selection":
        PlanetSelectMenu.planet_selection()



