import time

import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import Classes
import Game.Classes.player_class as player_class
import Game.Classes.planet_class as planet_class

earth_obj = planet_class.Planet("Earth")
Main_Menu_Options = {
    '1': 'Start Game',
    '2': 'Planet Selection',
    '3': 'Shops',
    '4': 'Exit'
}

def initialize_game():
    Player.Data["Name"] = input("Please enter your name: ")

def Game_Menu(game_player):
    import Game.Controllers.Menu_Controller as MenuController
    

    print(f"Welcome to the Game, {Player.Data['Name']}!")
    print("Please select an option from the menu below:")
    for Option in Main_Menu_Options:
        print(f"{Option} | {Main_Menu_Options[Option]}")

    try:    
        choice = int(input("Please select an option: "))
    except:
        print("That's not a number.")
        return True  # Continue loop

    # Conditional Statements
    if choice == 1:
        print("Starting Game...")
        MenuController.fetch_menu("Planet Menu", game_player, game_player.planet)
    elif choice == 2:
        MenuController.fetch_menu("Planet Selection", game_player)
    elif choice == 3:
        MenuController.fetch_menu("Shop", game_player)
    elif choice == 4:
        print("Exiting Game...")
        return False  # Exit loop
    return True

if __name__ == "__main__":
    initialize_game()
    player = player_class.Player_obj()
    while True:
        if not Game_Menu(player):
            break


