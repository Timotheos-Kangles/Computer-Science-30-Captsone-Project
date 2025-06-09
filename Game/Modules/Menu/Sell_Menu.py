import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
#import Game.Data.Data_Files.Player_Data as Player
import Game.Data.Data_Files.Ore_Data as Ore_Data

# import controllers
import Game.Controllers.Player_Controller as Player_Controller

def sell_ore(game_player):
    print("Pick a bar to sell or type 'back' to return: ")

    while True:
        for index, item in enumerate(list(game_player.inventory["Bars"].keys())):
            print(f"{index+1} | {item}")
        
        choice = (input("Choice: "))

        if type(choice) == str and not choice.isnumeric():
            if choice == 'back':
                break
            else:
                print('not an option')
                pass
        elif int(choice)-1 in range(len(list(game_player.inventory["Bars"].keys()))):
            choice = int(choice)
            if game_player.inventory["Bars"][list(game_player.inventory["Bars"])[choice-1]]["Amount"] > 0: # then the player has enough bars
                amount = game_player.inventory["Bars"][list(game_player.inventory["Bars"])[choice-1]]["Amount"]
                value = game_player.inventory["Bars"][list(game_player.inventory["Bars"])[choice-1]]["Value"]
                sell_amount = amount*value

                game_player.currency += sell_amount
                game_player.inventory["Bars"][list(game_player.inventory["Bars"])[choice-1]]["Amount"] = 0
                print(f"You sold {amount} {game_player.inventory["Bars"][list(game_player.inventory["Bars"])[choice-1]]}(s) and got {sell_amount} money")
            else:
                print(f"You don't have any {list(game_player.inventory["Bars"])[choice-1]}(s)")
        else:
            print('invalid option')
