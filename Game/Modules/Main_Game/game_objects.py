from Game.Classes.planet_class import Planet
from Game.Classes.player_class import Player_obj

# Initialize game objects
earth_obj = Planet("Earth")
mars_obj = Planet("Mars")
moon_obj = Planet("Moon")


player = Player_obj()
# earth specific objects
earth_grid1, vis_grid = earth_obj.create_grid(3, 3)
# mars specific objects
mars_grid1, vis_grid = mars_obj.create_grid(4, 4)
# moon specific objects
moon_grid1, vis_grid = moon_obj.create_grid(2, 2)
