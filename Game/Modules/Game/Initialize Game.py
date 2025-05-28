
import time

import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Classes.player_class as player_class 
# Import Controllers
import Game.Controllers.Menu_Controller as MenuController

Main_Menu_Options = {
    '1': 'Start Game',
    '2': 'Planet Selection',
    '3': 'Shops',
    '4': 'Exit'
}
def initialize_game():
    game_player = player_class.Player_obj()
    Player.Data["Name"] = input("Please enter your name: ")


    Game_Menu()  # Call Game_Menu after initialization

def Game_Menu():
    print(f"Welcome to the Game, {Player.Data['Name']}!")
    print("Please select an option from the menu below:")
    for Option in Main_Menu_Options:
        print(f"{Option} | {Main_Menu_Options[Option]}")

    try:    
        choice = int(input("Please select an option: "))
    except:
        print("That's not a number.")
        return  
    
    # Conditional Statements
    if choice == 1:
        print("Starting Game...")
    elif choice == 2:
        MenuController.fetch_menu("Planet Selection")
    elif choice == 3:
        MenuController.fetch_menu("Shop")
    elif choice == 4:
        print("Exiting Game...")
        print("Exiting Game...")

initialize_game()
Game_Menu()


