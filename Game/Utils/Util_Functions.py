#import tabulate

import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))

import Game.Data.Data_Files.Player_Data as Player


def debug_player_data(player):
    '''
    function that prints all the player data to the console for debugging purposes.
    '''
    print("Player Data")
    print("-------------------------")
    print(f"Name: {player.name}")
    print(f"Currency: {player.currency}")
    print(f"Health: {player.health}")
    print("-------------------------")
    print(f"Current Planet: {player.planet}")
    print(f"Unlocked Planets: {player.unlocked_planets}")
    print("--------------------------")
    print(f"Pickaxes: {player.inventory['Pickaxes']}")
    print(f"Drills: {player.inventory['Drills']}")
    print(f"Weapons: {player.inventory['Weapons']}")

    print(f"Ores: {player.inventory['Ores']}")
    print(f"Bars: {player.inventory['Bars']}")



    
