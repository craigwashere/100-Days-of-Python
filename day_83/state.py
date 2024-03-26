
class State:
    def __init__(self, old_state = None, mover = None):
        self.turn = ""
        self.depth = 0
        self.board = ['_' for i in range(9)]
        self.result = 'active'

        if  not old_state is None:
            self.board = old_state.board.copy()
            self.depth = old_state.depth
            self.result = old_state.result
            self.turn = old_state.turn
            
        if not mover is None:
            self.turn = mover['turn']
            self.board[mover['position']] = mover['turn']
            
            if mover['turn'] == 'O':
                self.depth += 1
                self.turn = 'X'
            else:
                self.turn = 'O'
        
    def empty_cells(self):
        empty_cells = []
        for i in range(9):
            if self.board[i] == '_':
                empty_cells.append(i)
                
        return empty_cells
        
    def gameOver(self):
       # print(f'gameOver->board: {self.board}')
        # check horizontally
        for i in range(0, 7, 3):
            if (self.board[i] != '_') and (self.board[i] == self.board[i+1]) and (self.board[i+1] == self.board[i+2]):
                self.result = self.board[i];
                return True;
    
    # check vertically
        for i in range(3):
            if(self.board[i] != '_') and (self.board[i] == self.board[i+3]) and (self.board[i+3] == self.board[i+6]):
                self.result = self.board[i];
                return True;
    
    # check diagonally
        if (self.board[4] != '_') and (((self.board[0] == self.board[4]) and (self.board[4] == self.board[8])) or 
              ((self.board[2] == self.board[4]) and (self.board[4] == self.board[6]))):
            self.result = self.board[4];
            return True;
    
    #if none of the win checks are met, check for a draw.
        available = self.empty_cells();
        if len(available) == 0:
            self.result = "draw";
            return True;
        else:
            return False;