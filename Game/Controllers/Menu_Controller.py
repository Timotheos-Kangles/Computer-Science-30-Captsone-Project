
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))


# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as EarthData
import Game.Data.Data_Files.Planet_Data.Mars_Data as MarsData

# Import Menu Modules
import Game.Modules.Shop.Shop_Menu as ShopMenu
import Game.Modules.Furnace.Furnace_Menu as FurnaceMenu

def fetch__menu(Menu, Planet):
    if Menu == "Tools":
        if Planet == "Earth":
            earth_tools = {
                "Pickaxes": EarthData.Tools["Pickaxes"],
                "Drills": EarthData.Tools["Drills"]
            }
            earth_weapons = EarthData.Tools["Weapons"]
            ShopMenu.shop_menu("Earth", earth_tools, earth_weapons)
        elif Planet == "Mars":
            mars_tools = {
                "Pickaxes": MarsData.Tools["Pickaxes"],
                "Drills": MarsData.Tools["Drills"]
            }
            mars_weapons = MarsData.Tools["Weapons"]
            ShopMenu.shop_menu("Mars", mars_tools, mars_weapons)
    elif Menu == "Furnace":
        FurnaceMenu.furnace_menu()


