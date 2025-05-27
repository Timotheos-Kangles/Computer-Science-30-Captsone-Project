
# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

def fetch_unlocked_planets():
    for index, planet in enumerate(planet.keys(), 1):
        print(f"{index} | {planet}")
        print(UtilVars.spacer)
        choice = int(input("What planet would you like to select?: "))
    pass


