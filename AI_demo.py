#
# AI Player for use in Connect Four  
#

import random  
from demo import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        return 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the 
        board, and that returns the index of the column with the maximum score
        """
        max_score = max(scores)
        cols = []
        
        for i in range(len(scores)):
            if scores[i] == max_score:
                cols += [i]
        if self.tiebreak == 'LEFT':
            return min(cols)
        elif self.tiebreak == 'RIGHT':
            return max(cols)
        elif self.tiebreak == 'RANDOM':
            return random.choice(cols)
    
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores 
        for the columns in b
        """
        scores = [0]*b.width
        
        for i in range(len(scores)):
            if b.can_add_to(i) == False:
                scores[i] = [-1]
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_score = opponent.scores_for(b)
                if max(opponent_score) == 0:
                    scores[i] = 100
                elif max(opponent_score) == 100:
                    scores[i] = 0
                else:
                    scores[i] = 50
                b.remove_checker(i)
        
        return scores
    
    
    def next_move(self, b):
        """overrides the next_move method that is inherited from Player"""
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
