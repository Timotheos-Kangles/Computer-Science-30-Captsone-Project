<<<<<<< HEAD
def alien_event():
    print('Your mining base is being attacked by aliens! You can \
          either defend or run away, coming back ')
=======
import random

def alien_event():
    '''
    how function works:
    - call function every 4 minute
    aliens invade your base, attempting to steal your ores and tools. You can defend or run away. Negotiation is not an option
    since aliens cannot communicate with you. Run away = lose 25 percent of your smelted ores. Fight can vary depending on weapon
    '''
    chance = 25
    player_money = 500
    if player_money > 1000 # requirement for event to trigger
        if random.randint(0, 100) < chance: # if some random number is less than 25
            print("You are being attacked by aliens! They are going to steal your ores! Either fight\
                  or run away. If you run away, you lose 25 percent of your ores. If you fight, you can win or lose depending\
                  on your weapon.")

    choice = int(input('What is your choice? (1 = fight, 2 = run away)'))

    if choice == 1:
        pass 
        # access player.weapons and winning is based on a chance based system
        # example: if player.weapon['win chance'] > random.randint(0, 100): aliens lose

    elif choice == 2:
        # loop through player ores and make each equal to .75 of what it was previously
        print('You ran away and lost some ores.'\
              'you now have this many ores')
        
        # loop through here
        
>>>>>>> 445bfd8204a086ab722345e14602541ede91baaf

    