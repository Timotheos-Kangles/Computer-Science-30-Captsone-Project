import random
def alien_event():
    '''
    how function works:
    - call function every 4 minute
    aliens invade your base, attempting to steal your ores and tools. You can defend or run away. Negotiation is not an option
    since aliens cannot communicate with you.
    '''
    chance = 25
    player_money = 500
    if player_money > 1000 # requirement for event to trigger
        if random.randint(0, 100) < chance:
            pass
            # what gets triggered


