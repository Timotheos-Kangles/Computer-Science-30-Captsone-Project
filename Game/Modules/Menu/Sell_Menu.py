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
    '''
    Handles the selling of bars to the game so the player can get money.
    '''
    print("Pick a bar to sell:")

    while True:
        for index, item in enumerate(list(game_player.inventory["Bars"].keys())):
            print(f"{index+1} | {item}")
        
        choice = (input("Choice or 'back': "))

        if type(choice) == str and not choice.isnumeric():
            if choice == 'back':
                break
            else:
                print('not an option')
                pass
        elif int(choice)-1 in range(len(list(game_player.inventory["Bars"].keys()))):
            choice = int(choice)
            player_bar = list(game_player.inventory["Bars"].keys())[choice-1]
            if game_player.inventory["Bars"][player_bar]["Amount"] > 0: # then the player has enough bars
                amount = game_player.inventory["Bars"][player_bar]["Amount"]
                value = game_player.inventory["Bars"][player_bar]["Value"]
                sell_amount = amount*value

                game_player.currency += sell_amount
                game_player.inventory["Bars"][player_bar]["Amount"] = 0
                print(f"You sold {amount} {game_player.inventory['Bars'][player_bar]}(s) and got {sell_amount} money")
            else:
                print(f"You don't have any {player_bar}(s)")
        else:
            print('invalid option')
