import Game.Data.Data_Files.Player_Data as Player

def currency_controller(type, amount):
    if type == "add":
        Player.Data["Currency"] += amount
        print(f"{amount} has been to your currency!")
    elif type == "remove":
        
        
    