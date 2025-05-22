import Earth_Data as Edata
import Tools_Menu as Tmenu
import Stroage_menu as Smenu
shop_menu_options = {
    1: 'Buy tools',
    2: 'Buy storage',
    3: 'Buy weapons'
}

def shop_menu(planet):
    print(f"Welcome to the {planet}'s best shop!")
    for key, item in shop_menu_options.items():
        print(f'{key} - {item}')

    try:
        choice = int(input("Choice: "))
    except:
        print("error")

    if choice == 1:
        Tmenu.Tool_Shop_Menu(planet)
    if choice == 2:
        # code here
        pass
    if choice == 3:
        pass
        # weapons




