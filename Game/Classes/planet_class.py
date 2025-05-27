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

