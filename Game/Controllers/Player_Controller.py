import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as Earth_Data
#from Game.Modules.Main_Game.Initialize_Game import player


def currency_controller(action, value, player):
    '''
    controls the player's currency based on the action and value provided.
    '''
    if action == "add":
        player.currency += value
    elif action == "remove":
        player.currency -= value
    else:
        print("Invalid action")


def inventory_controller(action, item, player):
    '''
    controls the player's inventory based on the action and item provided.
    '''
    if action == "add":
        if item in Earth_Data.Ores.keys():
            player.inventory['Ores'][item]['amount']+=1
        
        for i in Earth_Data.Tools.keys():
            if item in Earth_Data.Tools[i]:
                player.inventory[i].append(item)
    elif action == "remove":
        Player.Data["Inventory"].remove(item)
    else:
        print("Invalid action")


def planet_controller(planet):
    '''
    Handles the player's planet selection.
    '''
    if planet in Player.Data["Unlocked Planets"]:
        Player.Data["Planet"] = planet
        print(f"You have traveled to {planet}!")
    else:
        print(f"You have not unlocked {planet} yet.")


def fetch_grid(planet):
    if planet == "Earth":
        from Game.Modules.Main_Game.game_objects import earth_grid1
        return earth_grid1
    elif planet == "Mars":
        from Game.Modules.Main_Game.game_objects import mars_grid1
        return mars_grid1
    

def fetch_planet_obj(planet):
    if planet == "Earth":
        from Game.Modules.Main_Game.game_objects import earth_obj
        return earth_obj
    if planet == "Mars":
        from Game.Modules.Main_Game.game_objects import mars_obj
        print(f"DEBUG: Returning mars_obj: {mars_obj}")
        return mars_obj
    else:
        print(f"Planet {planet} not found.")
        return None