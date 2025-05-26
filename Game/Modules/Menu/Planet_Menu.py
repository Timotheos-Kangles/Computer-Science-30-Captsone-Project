

# Import Others
import Game.Utils.Util_Variables as UtilVars
how 
# Import Menu Modules
import Game.Modules.Menu.Tools_Menu as ToolShop
import Game.Modules.Menu.Weapons_Menu as WeaponShop
import Game.Modules.Menu.Furnace_Menu as FurnaceMenu
import Game.Modules.Menu.Shop_Menu as ShopMenu

# Import Controllers
import Game.Controllers.Menu_Controller as MenuController

Planet_Menu_Options = {
    1: 'Return to Main Menu',
    2: 'Shop',
    3: 'Furnace',

}

def planet_menu(planet):
    print(f"Welcome to {planet} Menu!")
    print(UtilVars.spacer)
    
    for key, option in Planet_Menu_Options.items():
        print(f"{key} | {option}")
    choice = int(input("Please select an option: "))

    if choice == 1:
        MenuController.fetch_menu("Main Menu")
    elif choice == 2:
        ShopMenu.shop_menu(planet)
    elif choice == 3:
        FurnaceMenu.furnace_menu(planet)
    else:
        print("Invalid option selected.")
    print("What would you like to do?")
    for key, option in Planet_Menu_Options.items():
        print(f"{key} | {option}")
    
    try:
        choice = int(input("Please select an option: "))
    except ValueError:
        print("That's not a number.")
        return
    
    if choice == 1:
        MenuController.fetch_menu("Main Menu")
    elif choice == 2:
        MenuController.fetch_menu("Tools", planet)
    elif choice == 3:
        FurnaceMenu.furnace_menu(planet)
    else:
        print("Invalid option. Please try again.")