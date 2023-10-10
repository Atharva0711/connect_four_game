#
# A Connect-Four Player class 
#  

from connect_code1 import Board

class Player: 
    
    def __init__(self, checker):
        """constructs a new Player object"""
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing a Player object"""
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """returns a one-character string representing the checker of the 
        Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move
        """
        while True:
            user_input = input('Enter a column: ')
            col_number = int(user_input)
            
            if b.can_add_to(col_number) == False:
                print('Try again!')
                print()
            elif b.can_add_to(col_number) == True:
                self.num_moves += 1
                return col_number             


