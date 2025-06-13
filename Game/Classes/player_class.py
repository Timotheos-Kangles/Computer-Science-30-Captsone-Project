# Import Data Files
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))


import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as Earth_Data
import random
import Game.Controllers.Planet_Controller as PlanetController
import Game.Controllers.Player_Controller as Player_Controller
import Game.Utils.Util_Functions as Util_Functions

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
        self.is_moving = False

    def movement(self, map_parameter, planet_obj):
        '''
        Handles player movement on the grid. map_parameter is the grid of the planet
        and planet_obj is the object of the planet that contains the grid and other methods.
        This method handles movement and mining tiles.
        '''
        while self.is_moving:
            #print("DEBUG before movement: map size =", len(map_parameter), "rows x", len(map_parameter[0]), "cols")
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
            elif choice == 'back':
                self.is_moving = False
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
        '''
        Mines the tile and handles oil explosion and pickaxe or drill type. 
        Also handles ore rarity. 
        '''
        oil_explosion_chance = 10 # percent chance of explosion
        player_planet_data = PlanetController.fetch_planet_data(self.planet)
        ore_list = list(player_planet_data.Ores.keys())
        for ore in player_planet_data.Ores.keys():

            for rarity in range(player_planet_data.Ores[ore]['Rarity'] - 1):
                ore_list.append(ore)

        #print(ore_list)
        #print('There might have been nothing in the list')

        # implement rarity of ores

        print(f"Your health is: {self.health}")

        if oil_explosion_chance > random.randint(0, 100):
            print("Oil explosion! You lost some health. Buy some items from the med store to heal up.")
            self.health -= 10 
            if self.health <= 0:
                print("You have died. Game over.")
                exit()
        else:
            mined_ore = random.choice(ore_list)
            mined_amount = None
            

                # implement price of pickaxe into yield

            if len(self.inventory['Pickaxes']) != 0 or len(self.inventory['Drills']) != 0:
                #print('The player has a pickaxe or a drill. we can mine.')
                if len(self.inventory["Drills"]) == 0: # then the player has no drills so we will look at the latest purchased pickaxe
                    if self.inventory["Pickaxes"][-1] == "Wooden Pickaxe":                # at the end of the list (index -1)
                        mined_amount = 1
                    elif self.inventory["Pickaxes"][-1] == "Iron Pickaxe":
                        mined_amount = 2
                    elif self.inventory["Pickaxes"][-1] == "Golden Pickaxe":
                        mined_amount = 3
                else:
                    if self.inventory["Drills"][-1] == "Basic Drill":
                        mined_amount = 10
                    elif self.inventory["Drills"][-1] == "Advanced Drill":
                        mined_amount = 20

                # add to inventory
                #print(f"DEBUG: mined_ore = {mined_ore}, mined_amount = {mined_amount}")
                self.inventory['Ores'][mined_ore]['Amount'] += mined_amount
                print(f"You mined {mined_amount} {mined_ore}! and now have {self.inventory['Ores'][mined_ore]['Amount']} in your inventory.")
            else:
                print("You don't have any pickaxes or drills! Go buy some at the shop!")

