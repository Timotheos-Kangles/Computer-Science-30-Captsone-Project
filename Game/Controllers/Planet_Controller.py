import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as Earth_Data
import Game.Data.Data_Files.Planet_Data.Mars_Data as Mars_Data
import Game.Data.Data_Files.Planet_Data.Moon_Data as Moon_Data

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# import initializated objects
#   from Game.Modules.Main_Game.game_objects import earth_obj, mars_obj


def fetch_unlocked_planets():
    '''
    gets the unlocked planets from the player data
    '''
    for index, planet in enumerate(planet.keys(), 1):
        print(f"{index} | {planet}")
        print(UtilVars.spacer)
        choice = int(input("What planet would you like to select?: "))
    pass


def fetch_planet_data(planet):
    '''
    Returns the correct planet data based on the planet name.
    '''
    if planet == 'Earth':
        return Earth_Data
    elif planet == 'Mars':
        return Mars_Data
    elif planet == 'Moon':
        return Moon_Data


