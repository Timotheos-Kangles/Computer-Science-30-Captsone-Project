import Player_Data

class Player():
    def __init__(self):
        self.currency = Player_Data.Data['Currency']
        self.pl_x = 0 # player coordinates for movement
        self.pl_y = 0
        self.planet = Player_Data.Data['Planet']

    def movement(self, map):
        choice = input('W A S D to move: ').lower()

        if choice == 'w':
            pass
        elif choice == 'd':
            pass

    