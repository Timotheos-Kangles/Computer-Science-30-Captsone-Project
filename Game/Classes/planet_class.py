
# Import Libraries
import time
import random
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Classes
import Game.Classes.player_class as PClass


class Planet():
    def __init__(self, name):
        self.ores ={ 
            "Copper Ore": {
                "Value": 5,
                "Smelting Time": 5,  # Time in seconds to smelt
                "Smelting Ratio": 3,  # Number of ore needed for 1 bar
                "Smelting Yield": {
                    "Copper Bar": 1  
                },
            }
        }
        self.pickaxes = {}
        self.drills = {}
        self.weapons = {}

        self.size = (0, 0)  # Default size, Length and Width
        self.events = []  # List of events on the planet
        
    
    def create_grid(self, length, width):
        grid = []
        for i in range(length):
            grid.append([])
            for j in range(width):
                grid[i].append(None)
        return grid

    def planet_event(self):
        player = PClass.player_class()
        
        if player.currency > 500:
            print("Player has more than 500 currency")






