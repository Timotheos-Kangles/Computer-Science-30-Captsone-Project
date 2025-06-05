import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))

# Other
import time
import random


# Events
import Game.Modules.Events.Alien_Event as Alien_Event
import Game.Modules.Events.Pirate_Event as Pirate_Event

# Player Data
import Game.Data.Data_Files.Player_Data as Player

last_event_time = 0

Events = {
    "Alien_Event": {
        "Trigger_Chance": 25,    # % Chance
        "Currency_Req": 2500,    # 
        "Cooldown": 240,         #  (4 minutes)
        "Last_Event_Time": 0,    # Last time the event was triggered
        "Function": Alien_Event.alien_event
    },
    "Pirate_Event": {
        "Trigger_Chance": 25,    # % Chance
        "Currency_Req": 2500,    # 
        "Cooldown": 240,         #  (4 minutes)
        "Last_Event_Time": 0,    # Last time the event was triggered
        "Function": Pirate_Event.pirate_event
    }
}

 
def trigger_event(event_name):
    event = Events[event_name]
    current_time = time.time()
    time_since_last = current_time - event["Last_Event_Time"]
    
    if time_since_last < event["Cooldown"]:
        remaining = int(event["Cooldown"] - time_since_last)
        print(f"{event_name} not detected... Next possible event in {remaining} seconds")
        return
    
    if Player.Data["Currency"] < event["Currency_Req"]:
        return
    
    if random.randint(1, 100) <= event["Trigger_Chance"]:
        Events[event_name]["Last_Event_Time"] = current_time
        event["Function"]()
