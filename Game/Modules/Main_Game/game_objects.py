from Game.Classes.planet_class import Planet
from Game.Classes.player_class import Player_obj

# Initialize game objects
earth_obj = Planet("Earth")
mars_obj = Planet("Mars")
player = Player_obj()

# earth specific objects
earth_grid = earth_obj.create_grid(3, 3)
print("DEBUG: earth_obj.grid size =", len(earth_obj.grid), "rows x", len(earth_obj.grid[0]), "cols")