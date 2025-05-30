import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Others
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player


def planet_selection(game_player):
    print("Available Planets:")
    print(UtilVars.spacer)
    for index, planet in enumerate(Player.Data["Unlocked Planets"], 1):
        print(f'{index} | {planet}')
    print(UtilVars.spacer)
    
    try:
        choice = int(input("Select a planet to set as spawn: "))
        if choice in range(1, len(Player.Data["Unlocked Planets"]) + 1):
            selected_planet = Player.Data["Unlocked Planets"][choice - 1]
            print(f"Traveling to {selected_planet}...")
            Player.Data["Current Planet"] = selected_planet
            game_player.planet = selected_planet
            print(Player.Data["Current Planet"])
            return selected_planet
        else:
            print("Invalid planet selection.")
            return planet_selection()
    except ValueError:
        print("Please enter a valid number.")
        return planet_selection()
