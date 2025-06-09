from Game.Classes.planet_class import Planet
from Game.Classes.player_class import Player_obj

# global variables


# Initialize game objects
earth_obj = Planet("Earth")
mars_obj = Planet("Mars")
player = Player_obj()

# earth specific objects
earth_grid1, vis_grid = earth_obj.create_grid(3, 3)

# mars specific objects
mars_grid1, vis_grid = mars_obj.create_grid(4, 4)

#print("DEBUG: earth_obj.grid size =", len(earth_obj.grid), "rows x", len(earth_obj.grid[0]), "cols")
#print("DEBUG: earth_grid1 size =", len(earth_grid1), "rows x", len(earth_grid1[0]), "cols")
print("DEBUG: mars_obj =", mars_obj)