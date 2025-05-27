import pyfiglet
import time

import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import Controllers
import Game.Controllers.Menu_Controller as MenuController

Main_Menu_Options = {
    '1': 'Start Game',
    '2': 'Planet Selection',
    '3': 'Shops',
    '4': 'Exit'
}
def initialize_game():
    #font = pyfiglet.Figlet(font = 'block', width = 50)
    #print(font.renderText('This is a test text.')) 
    
    print('Welcome to ')

#initialize_game()
    font = pyfiglet.Figlet(font = 'doh', width = 50)
    print(font.renderText('This is a test text.')) 
    Game_Menu()  # Call Game_Menu after initialization

def Game_Menu():
    print("Welcome to the Game!")
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
        print("Planet Selection...")
    elif choice == 3:
        MenuController.fetch_menu(Player.Data["Current Planet"])
    elif choice == 4:
        print("Exiting Game...")
        print("Exiting Game...")

Game_Menu()