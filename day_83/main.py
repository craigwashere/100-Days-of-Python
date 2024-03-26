import tkinter as tk
from PIL import ImageTk,Image
from ai import AI
from state import State
from game import Game

rows, cols = (3, 3)

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 200):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 200):
        c.create_line([(0, i), (w, i)], tag='grid_line')

def draw_image(row, col, img):
    c.create_image(col,row, anchor=tk.NW, image=img)
        
def leftclick(event):
    print('leftclick')
    row = int(event.y/200)
    col = int(event.x/200)

    player_position = row*rows+col
 
    if not game.isValid(player_position):
        return
        
    new_state = State(game.current_state, {'turn': 'X', 'position': player_position})
    game.advanceTo(new_state)

    draw_image(row*200, col*200, x_img)

    ai_move = game.ai.take_move(game.current_state)
    new_state = State(game.current_state, {'turn': 'O', 'position': ai_move})
    game.advanceTo(new_state)

    row = int(ai_move/3)
    col = int(ai_move%3)
    draw_image(row*200, col*200, o_img)
    
    if game.current_state.gameOver():
        print('game over')
        draw_image(0, 0, you_lose_image)
        c.unbind('<Button-1>')
    print(f'game status: {game.current_state.result}')

    
root = tk.Tk()

c = tk.Canvas(root, height=600, width=600, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)
c.bind("<Button-1>", leftclick)

x_img = ImageTk.PhotoImage(Image.open('X.png').resize((200,200), Image.Resampling.HAMMING))
o_img = ImageTk.PhotoImage(Image.open('O.png').resize((200,200), Image.Resampling.HAMMING))
you_lose_image = ImageTk.PhotoImage(Image.open('you_lose.png').resize((600,600), Image.Resampling.HAMMING))

ai = AI()
game = Game(ai)
ai.game = game

root.mainloop()