import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

import random
import time

# Import Utilities
import Game.Utils.Util_Variables as UtilVars

# Import Data Files
import Game.Data.Data_Files.Player_Data as Player

last_event_time = 0

def alien_event():
    '''
    how function works:
    - call function every 4 minute
    aliens invade your base, attempting to steal your ores and tools. You can defend or run away. Negotiation is not an option
    since aliens cannot communicate with you. Run away = lose 25 percent of your smelted ores. Fight can vary depending on weapon
    '''
    global last_event_time
    Trigger_Chance = 25
    Currency_Req = 1000
    Cooldown = 240  # 4 minutes in seconds
    
    # Check cooldown
    current_time = time.time()
    time_since_last = current_time - last_event_time
    
    if time_since_last < Cooldown:
        remaining = int(Cooldown - time_since_last)
        print(f"Alien invasion not detected... Next possible invasion in {remaining} seconds")
        return
    
    randomchance = random.randint(0, 100)
    
    if Player.Data["Currency"] > Currency_Req:
        print(randomchance)
        if randomchance < Trigger_Chance: # if some random number is less than 25
            print(randomchance)
            print(UtilVars.spacer)
            print("You are being attacked by aliens! They are going to steal your ores! \nEither fight run away. If you run away, you lose 25 percent of your ores. \nIf you fight, you can win or lose depending on your weapon.")
            print(UtilVars.spacer)
            choice = int(input('What is your choice? (1 / 2): '))
            print(UtilVars.spacer)

            if choice == 1:
                weapons = Player.Data["Inventory"]["Weapons"]
                if not weapons:
                    print("You have no weapons to fight with! The aliens steal some of your ores...")
                    return
                    
                print("\nAvailable weapons:")
                for index, weapon in enumerate(weapons.keys(), 1):
                    print(f"{index} | {weapon}")
                
                try:
                    weapon_choice = int(input("Select a weapon to fight with: ")) - 1
                    if weapon_choice in range(len(weapons)):
                        selected_weapon = list(weapons.keys())[weapon_choice]
                        weapon_data = weapons[selected_weapon]
                        
                        # Combat chance calculation
                        win_chance = weapon_data.get("Win Chance", 50)  # Default 50% if not specified
                        if random.randint(1, 100) <= win_chance:
                            print(f"You successfully fought off the aliens with your {selected_weapon}!")
                            print("Your ores are safe.")
                        else:
                            print(f"Despite using your {selected_weapon}, the aliens overwhelmed you!")
                            print("You lost some ores in the battle...")
                            # Handle ore loss like running away
                    else:
                        print("Invalid weapon selection. The aliens take advantage of your hesitation!")
                        # Handle ore loss like running away
                except ValueError:
                    print("Invalid input. The aliens attack while you fumble with your weapons!")
                    # Handle ore loss like running away

            elif choice == 2:
                print("You choose to run away from the aliens...")
                print(UtilVars.spacer)
                for ore_name, ore_data in Player.Data["Inventory"]["Ores"].items():
                    ore_amount = ore_data.get("Amount", 0)  # Get the amount from the ore dictionary
                    if ore_amount > 0:
                        # Randomly choose between 10% and 30% loss
                        loss_percentage = random.choice([0.10, 0.30])
                        ore_loss = int(ore_amount * loss_percentage)
                        
                        # Update ore amount
                        Player.Data["Inventory"]["Ores"][ore_name]["Amount"] -= ore_loss
                        
                        print(f"> You lost {ore_loss} {ore_name} ({int(loss_percentage * 100)}% lost) |  Remaining: {Player.Data['Inventory']['Ores'][ore_name]['Amount']}")
                
                print("\nYou managed to escape, but at what cost...")
            

alien_event()