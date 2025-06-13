
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
    
    def create_grid(self, rows, cols):
        '''
        Creates a grid and a copy for visualization. Rows and cols integers 
        and are the dimensions.
        '''
        self.grid = []  # Reset grid
        for i in range(rows):
            self.grid.append([])
            for j in range(cols):
                self.grid[i].append(None)

        self.visualize_grid = copy.deepcopy(self.grid)  # Create a visual grid for display
        return self.grid, self.visualize_grid
    def visual_grid(self):
        '''
        Uses the tabulate library to print the grid in a readable format.
        '''
        print(tabulate.tabulate(self.visualize_grid, tablefmt="rounded_grid"))
        if len(self.visualize_grid) == 0:
            print("Looks like the code for creating the grid is not working properly.")
    
    def update_player_on_grid(self, pl_x, pl_y):
        '''
        Refreshes the grid to show the player's position.
        pl_x and pl_y are the player's coordinates on the grid.
        '''
    # Clear grid
        for y in range(len(self.visualize_grid)):
            for x in range(len(self.visualize_grid[0])):
                self.visualize_grid[y][x] = None
        # Set player position
        self.visualize_grid[pl_y][pl_x] = "P"
        return self.visualize_grid







