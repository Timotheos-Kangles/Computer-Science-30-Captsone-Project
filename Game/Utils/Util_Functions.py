#import tabulate

import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))

import Game.Data.Data_Files.Player_Data as Player


def create_map(length, width):
    grid = []
    for i in range(length):
        grid.append([])

        for j in range(width):
            grid[i].append(None)
    return grid
#print(tabulate.tabulate(create_map(5,5), tablefmt='rounded_grid'))

def debug_player_data(player):
    '''
    print("Player Data")
    print("-------------------------")
    print(f"Name: {Player.Data['Name']}")
    print(f"Currency: {Player.Data['Currency']}")
    print(f"Health: {Player.Data['Health']}")
    print("-------------------------")
    print(f"Current Planet: {Player.Data['Current Planet']}")
    print(f"Unlocked Planets: {Player.Data['Unlocked Planets']}")
    print("--------------------------")
    print(f"Pickaxes: {Player.Data['Inventory']['Pickaxes']}")
    print(f"Drills: {Player.Data['Inventory']['Drills']}")
    print(f"Weapons: {Player.Data['Inventory']['Weapons']}")
    print(f"Ores: {Player.Data['Inventory']['Ores']}")
    print(f"Bars: {Player.Data['Inventory']['Bars']}")
    print("--------------------------")
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



    
