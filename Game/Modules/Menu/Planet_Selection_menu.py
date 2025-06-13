import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Others
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player


def planet_selection(game_player):
    '''
    Function handles selecting a planet to set as spawn point. 
    game_player is the player object.
    '''
    print("Available Planets:")
    print(UtilVars.spacer)
    for index, planet in enumerate(Player.Data["Unlocked Planets"], 1):
        print(f'{index} | {planet}')
    print(UtilVars.spacer)
    
    try:
        choice = int(input("Select a planet to set as spawn: "))
        if choice == 1:
            selected_planet = Player.Data["Unlocked Planets"][choice - 1]
            print(f"Traveling to {selected_planet}...")
            Player.Data["Current Planet"] = selected_planet
            game_player.planet = selected_planet
            print(Player.Data["Current Planet"])
            return selected_planet
        elif choice == 2 and game_player.currency > 0:
            selected_planet = Player.Data["Unlocked Planets"][choice - 1]
            print(f"Traveling to {selected_planet}...")
            Player.Data["Current Planet"] = selected_planet
            game_player.planet = selected_planet
            print(Player.Data["Current Planet"])
            return selected_planet
        elif choice == 3 and game_player.currency > 0:
            selected_planet = Player.Data["Unlocked Planets"][choice - 1]
            print(f"Traveling to {selected_planet}...")
            Player.Data["Current Planet"] = selected_planet
            game_player.planet = selected_planet
            print(Player.Data["Current Planet"])
            return selected_planet            
        else:
            print("Invalid planet selection. You need 2000 money to unlock the Moon and 4000 money to unlock Mars.")
            return planet_selection(game_player)
    except ValueError:
        print("Please enter a valid number.")
        return planet_selection(game_player)
