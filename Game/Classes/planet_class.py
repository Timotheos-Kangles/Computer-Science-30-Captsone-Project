
# Import Libraries
import time
import random
import copy 
import sys
import tabulate
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Classes
import Game.Classes.player_class as PClass



class Planet():
    def __init__(self, name):
        # core gameplay variables
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
        
        # grid variables
        self.grid = []
        self.visualize_grid = []
    
    def create_grid(self, length, width):

        for i in range(length):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(None)

        self.visualize_grid = copy.deepcopy(self.grid)  # Create a visual grid for display

    def visual_grid(self):
        print(tabulate.tabulate(self.visualize_grid, tablefmt="rounded_grid"))

    def planet_event(self):
        player = PClass.player_class()
        
        if player.currency > 500:
            print("Player has more than 500 currency")






