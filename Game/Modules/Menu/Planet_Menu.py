import sys
from pathlib import Path


root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Others
import Game.Utils.Util_Variables as UtilVars
 
# Import Menu Modules
import Game.Modules.Menu.Tools_Menu as ToolShop
import Game.Archive.Weapons_Menu as WeaponShop
import Game.Modules.Menu.Furnace_Menu as FurnaceMenu
import Game.Modules.Menu.Shop_Menu as ShopMenu
import Game.Modules.Menu.Sell_Menu as Sell_Menu
# Import Controllers
    #import Game.Controllers.Menu_Controller as MenuController
import Game.Controllers.Planet_Controller as Planet_Controller
import Game.Controllers.Player_Controller as Player_Controller
# import objects
from Game.Modules.Main_Game.game_objects import earth_grid1

Planet_Menu_Options = {
    1: 'Return to Main Menu',
    2: 'Shop',
    3: 'Furnace',
    4: 'Mining Area',
    5: 'Sell Refined Ores'

}

def planet_menu(game_player, planet):
    '''
    Menu options for when the player is on a planet. Planet is the name of the planet
    and game_player is the player object.
    '''
    while True:
        print(f"Welcome to {planet} Menu!")
        print(UtilVars.spacer)

        for key, option in Planet_Menu_Options.items():
            print(f"{key} | {option}")

        try:
            choice = int(input("Please select an option: "))
        except:
            choice = 'error'

        if choice == 1:
            #MenuController.fetch_menu("Main Menu")
            return "Main Menu"
        elif choice == 2:
            #ShopMenu.shop_menu(planet)
            ShopMenu.shop_menu(planet, game_player)
        elif choice == 3:
            #FurnaceMenu.furnace_menu(planet)
            FurnaceMenu.furnace_menu(game_player)
        elif choice == 4:
            game_player.is_moving = True
            while game_player.is_moving:
                #print("DEBUG: map size =", len(Player_Controller.fetch_grid(game_player.planet)), "rows x", len(Player_Controller.fetch_grid(game_player.planet)[0]), "cols")
                #print(f"Players current planet is: {game_player.planet}")
                #print(f"Players current object is: {Planet_Controller.fetch_planet_obj(game_player.planet)} ")
                #print("DEBUG: About to call fetch_planet_obj")
                Player_Controller.fetch_planet_obj(game_player.planet).visual_grid()
                game_player.movement(Player_Controller.fetch_grid(game_player.planet), Player_Controller.fetch_planet_obj(game_player.planet))  
                #print("DEBUG: map size =", len(Player_Controller.fetch_grid(game_player.planet)), "rows x", len(Player_Controller.fetch_grid(game_player.planet)[0]), "cols")
        elif choice == 5:
            Sell_Menu.sell_ore(game_player)
        elif choice == 'error':
            print("Invalid option selected.")
