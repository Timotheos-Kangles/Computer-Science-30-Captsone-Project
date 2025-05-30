import time
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import shared game objects
from Game.Modules.Main_Game.game_objects import earth_obj, mars_obj, player

Main_Menu_Options = {
    '1': 'Start Game',
    '2': 'Planet Selection',
    '3': 'Shops',
    '4': 'Casino',
    '5': 'Exit'
}

def initialize_game():
    Player.Data["Name"] = input("Please enter your name: ")

def Game_Menu(game_player):
    import Game.Controllers.Menu_Controller as MenuController
    

    print(f"Welcome to the Game, {Player.Data['Name']}!")
    print(f"Your planet is: {game_player.planet}")
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
        MenuController.fetch_menu("Planet Selection", game_player, game_player.planet)
    elif choice == 3:
        MenuController.fetch_menu("Shop", game_player, game_player.planet)
    elif choice == 3:
        print("Opening Casino...")
        print("Casino is not implemented yet.")
    elif choice == 5:
        print("Exiting Game...")
        return False  # Exit loop
    return True

#player = player_class.Player_obj()
if __name__ == "__main__":
    initialize_game()
    while True:
        if not Game_Menu(player):
            break

from Game.Classes.planet_class import Planet
from Game.Classes.player_class import Player_obj

# Initialize game objects
earth_obj = Planet("Earth")
mars_obj = Planet("Mars")
player = Player_obj()
