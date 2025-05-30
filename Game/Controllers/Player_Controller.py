import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Planet_Data.Earth_Data as Earth_Data
#from Game.Modules.Main_Game.Initialize_Game import player
def currency_controller(action, value):
    if action == "add":
        Player.Data["Currency"] += value
    elif action == "remove":
        Player.Data["Currency"] -= value
    else:
        print("Invalid action")

def inventory_controller(action, item, player):
    if action == "add":
        if item in Earth_Data.Ores.keys():
            player.inventory['Ores'][item]['amount']+=1
        
        for i in Earth_Data.Tools.keys():
            if item in Earth_Data.Tools[i]:
                player.inventory['Tools'][i]['amount'].append(item)
    elif action == "remove":
        Player.Data["Inventory"].remove(item)
    else:
        print("Invalid action")

def planet_controller(planet):
    if planet in Player.Data["Unlocked Planets"]:
        Player.Data["Planet"] = planet
        print(f"You have traveled to {planet}!")
    else:
        print(f"You have not unlocked {planet} yet.")

def fetch_player_data(player):
    return Player
