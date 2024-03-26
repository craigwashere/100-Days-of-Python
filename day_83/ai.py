from state import State

class AI:
    def __init__(self):
        self.game = {}
        self.next_move = -1
        
    # This is the minimax function. It considers all the possible ways the game can go and returns
    # the value of the board
    def minimax(self, state):
        if state.gameOver():
            return self.game.score(state)

        scores = []
        moves = state.empty_cells()
        
        for move in moves:
            possible_state = State(state, {'turn': state.turn, 'position': move})

            scores.append(self.minimax(possible_state))
        
        if state.turn == 'X':
            max = self.find_max_index(scores)
            self.next_move = moves[max]
            return scores[max]
        else:
            min = self.find_min_index(scores)
            self.next_move = moves[min]
            return scores[min]

    # This will return the best possible move for the player
    def take_move(self, state):
        state.turn = 'O'
        self.minimax(state)
        
        return self.next_move
        
    def find_min_index(self, arr):
        min_index = 0
        min = 0
        
        for i in range(len(arr)):
            if arr[i] <= min:
                min_index = i
                min = arr[i]
                
        return min_index

    def find_max_index(self, arr):
        max_index = 0
        max = 0
        
        for i in range(len(arr)):
            if arr[i] >= max:
                max_index = i
                max = arr[i]
                
        return max_index
    