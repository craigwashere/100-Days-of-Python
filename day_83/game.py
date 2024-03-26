from ai import AI
from state import State

class Game:
    def __init__(self, AI):
        self.ai = AI
        self.current_state = State()
        self.current_state.turn = 'X'
        
        self.status = 'start'
        
    def advanceTo(self, state):
        self.current_state = state

    def isValid(self, space):
        return (self.current_state.board[space] == '_')
        
    def score(self, state):
        if state.result == 'X':
            return 10 - state.depth
        elif state.result == 'O':
            return -10 + state.depth
        else:
            return 0