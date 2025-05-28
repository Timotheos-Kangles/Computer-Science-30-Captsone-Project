# Import Data Files
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))


import Game.Data.Data_Files.Player_Data as Player
import random
import Game.Controllers.Planet_Controller as PlanetController
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

    def movement(self, map):
        choice = input('W A S D to move: ').lower()

        if choice == 'w':
            self.pl_y -= 1
        elif choice == 'a': 
            self.pl_x -= 1
        elif choice == 's':
            self.pl_y += 1
        elif choice == 'd':
            self.pl_x += 1
        else:
            print('Invalid input. Please use W, A, S, or D to move.')
            return
        # Check boundaries
        if self.pl_x < 0:
            self.pl_x = 0
        elif self.pl_x >= len(map[0]):
            self.pl_x = len(map[0]) - 1
        if self.pl_y < 0:
            self.pl_y = 0
        elif self.pl_y >= len(map):
            self.pl_y = len(map) - 1
            
    def mine_tile(self):
        oil_explosion_chance = 10 # percent chance of explosion
        player_planet_data = PlanetController.fetch_planet_data(self.planet)
        ore_list = list(player_planet_data.Ores.keys())
        print(player_planet_data.Ores) # debug line
        print(player_planet_data.Ores['Blank Ore']['Rarity']) # debug line
        for ore in player_planet_data.Ores.keys():
            print('ran loop for ore once') # debug line
            for rarity in range(player_planet_data.Ores[ore]['Rarity'] - 1):
                print('ran loop for rarity twice')  # debug line
                print("Entered mine_tile()")
                print('appended ore to ore_list')
                ore_list.append(ore)

        print(ore_list)
        print('There might have been nothing in the list')

        # implement rarity of ores

        if oil_explosion_chance > random.randint(0, 100):
            print("Oil explosion! You lost some health.")
            self.health -= 10
            if self.health <= 0:
                print("You have died. Game over.")
                return False
        else:
            mined_ore = random.choice(ore_list)
            print(f"You mined {mined_ore}!")
            self.inventory['Ores'][mined_ore]['Amount'] += 1


print("Creating player...")
test_player_obj = Player_obj()
print("Player created.")
test_player_obj.mine_tile()