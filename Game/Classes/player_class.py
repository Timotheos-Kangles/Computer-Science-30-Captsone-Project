# Import Data Files
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))


import Game.Data.Data_Files.Player_Data as Player
import random
import Game.Controllers.Planet_Controller as PlanetController
import Game.Controllers.Player_Controller as Player_Controller
import Game.Utils.Util_Functions as Util_Functions
print('RUnning script')
class Player_obj():
    def __init__(self):
        self.currency = Player.Data['Currency']
        self.health = Player.Data['Health']
        self.name = Player.Data['Name']
        self.inventory = Player.Data['Inventory']
        self.pl_x = 0 # player coordinates for movement
        self.pl_y = 0
        self.planet = Player.Data['Current Planet']
        self.unlocked_planets = Player.Data['Unlocked Planets']
        self.alive = True # Player status so game ends when player dies
    def movement(self, map_parameter, planet_obj):

        while True:
            print("DEBUG before movement: map size =", len(map_parameter), "rows x", len(map_parameter[0]), "cols")
            print(f"Player Coordinates: ({self.pl_x}, {self.pl_y})")
            planet_obj.update_player_on_grid(self.pl_x, self.pl_y)
            planet_obj.visual_grid()
            choice = input('W A S D, back to go back: ').lower()

            if choice == 'w':
                self.pl_y -= 1
            elif choice == 'a': 
                self.pl_x -= 1
            elif choice == 's':
                self.pl_y += 1
            elif choice == 'd':
                self.pl_x += 1
            elif choice == 'm':
                self.mine_tile()
            else:
                print('Invalid input. Please use W, A, S, or D to move.')
                pass
            # Check boundaries
            if self.pl_x < 0:
                self.pl_x = 0
            elif self.pl_x >= len(map_parameter[0]):
                self.pl_x = len(map_parameter[0]) - 1
            if self.pl_y < 0:
                self.pl_y = 0
            elif self.pl_y >= len(map_parameter):
                self.pl_y = len(map_parameter) - 1
            
    def mine_tile(self):
        oil_explosion_chance = 80 # percent chance of explosion
        player_planet_data = PlanetController.fetch_planet_data(self.planet)
        ore_list = list(player_planet_data.Ores.keys())
        for ore in player_planet_data.Ores.keys():

            for rarity in range(player_planet_data.Ores[ore]['Rarity'] - 1):
                ore_list.append(ore)

        #print(ore_list)
        #print('There might have been nothing in the list')

        # implement rarity of ores

        if oil_explosion_chance > random.randint(0, 100):
            print("Oil explosion! You lost some health.")
            self.health -= 10
            if self.health <= 0:
                print("You have died. Game over.")
                self.alive = False
                return False
        else:
            mined_ore = random.choice(ore_list)
            print(f"You mined {mined_ore}!")
            self.inventory['Ores'][mined_ore]['Amount'] += 1
        Util_Functions.debug_player_data(self)
            


#print("Creating player...")
#test_player_obj = Player_obj()
#print("Player created.")
#test_player_obj.mine_tile()