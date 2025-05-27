<<<<<<< HEAD

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


    



=======
import Utils
import Planet_Data
import copy
class Planet:
    def __init__(self, data_name, player): # for example, data_name could be 'Earth_Data'
        ores = Planet_Data.data_name.Ores
        tools = Planet_Data.data_name.Tools
        weapons = Planet_data.Tata_name
        event = Game.Modules.Events.Alien_Event
        self.player = player
    def map(self, size):
        tile_map = Utils.create_grid(5, 5)
        visual_tile_map = copy.deepcopy(tile_map)

    def grid_visual(self);
        '''
        loop through tiles and delete '^' marker that marks where the player was previously
        check for any map markers such as 'm' denoting where mining area is
        '''
        pass



    def event(self):
        self.event()
>>>>>>> 445bfd8204a086ab722345e14602541ede91baaf

