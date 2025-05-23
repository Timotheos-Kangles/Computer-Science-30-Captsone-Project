import pyfiglet
import time

Menu_Options = {
    '1': 'Start Game',
    '2': 'Planet Selection',
    '3': 'Store',
    '4': 'Exit'
}
def initialize_game():
    font = pyfiglet.Figlet(font = 'doh', width = 50)
    print(font.renderText('This is a test text.')) 
    

initialize_game()

def Game_Menu():
    print("Welcome to the Game!")
    for Option in Menu_Options:
        print(f"{Option} | {Menu_Options[Option]}")

    try:    
        choice = int(input("Please select an option: "))
    except:
        print("That's not a number.")
    
    # Condtional Statements
    if choice == 1:
        print("Starting Game...")
    elif choice == 2:
        print("Planet Selection...")
    elif choice == 3:
        print("Store...")
    elif choice == 4:
        print("Exiting Game...")

Game_Menu()