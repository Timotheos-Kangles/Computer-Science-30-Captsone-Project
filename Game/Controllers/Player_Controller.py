import Game.Data.Data_Files.Player_Data as Player

def currency_controller(action, value):
    if action == "add":
        Player.Data["Currency"] += value
    elif action == "remove":
        Player.Data["Currency"] -= value
    else:
        print("Invalid action")

def inventory_controller(action, item):
    if action == "add":
        Player.Data["Inventory"].append(item)
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
