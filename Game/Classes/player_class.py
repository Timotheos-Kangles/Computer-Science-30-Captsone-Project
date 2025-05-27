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
            self.ply -= 1
        elif choice == 'a': 
            self.pl_x -= 1
        elif choice == 's':
            self.pl_y += 1
        elif choice == 'd':
            self.pl_x += 1
        else:
            print('Invalid input. Please use W, A, S, or D to move.')
            return
        # Check boundaries
        if self.pl_x < 0:
            self.pl_x = 0
        elif self.pl_x >= len(map[0]):
            self.pl_x = len(map[0]) - 1
        if self.pl_y < 0:
            self.pl_y = 0
        elif self.pl_y >= len(map):
            self.pl_y = len(map) - 1
            
 
    