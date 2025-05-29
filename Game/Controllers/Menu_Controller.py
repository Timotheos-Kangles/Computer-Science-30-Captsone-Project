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
#import Game.Modules.Menu.Planet_Menu as Planet_Menu

def fetch_menu(Menu, game_player, Planet=None):
    
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
    
    if Menu == "Furnace":
        FurnaceMenu.furnace_menu()
    elif Menu == "Shop":
        ShopMenu.shop_menu("Earth", EarthData.Tools, EarthData.Tools["Weapons"])
    elif Menu == "Planet Selection":
        PlanetSelectMenu.planet_selection()
    elif Menu == "Planet Menu":
        from Game.Modules.Menu.Planet_Menu import planet_menu
        next_menu = planet_menu(game_player, Planet)
        if next_menu == "Main Menu":
            fetch_menu("Main Menu", game_player)
        # handle other returns as needed


