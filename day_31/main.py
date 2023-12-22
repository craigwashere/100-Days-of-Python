import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

PADDING = 50

LANGUAGE_LOCATION_X = 400
LANGUAGE_LOCATION_Y = 150
LANGUAGE_FONT = ("Ariel", 40, "italic")

WORD_LOCATION_X = 400
WORD_LOCATION_Y = 263
WORD_FONT = ("Ariel", 60, "bold")

CARD_HEIGHT = 526
CARD_WIDTH = 800

try:
    word_list = pandas.read_csv("data/words_to_learn.csv").to_dict(orient='records')
except FileNotFoundError:
    word_list = pandas.read_csv("data/french_words.csv").to_dict(orient='records')
    
current_card = {}

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(word_list)
    language = list(current_card.keys())[0]
    card_canvas.itemconfig(language_label, text=language, fill="black")
    card_canvas.itemconfig(word_label, text=current_card[language], fill="black")
    card_canvas.itemconfig(card_id, image=front_card_image)
    timer = window.after(3000, show_back)
    
def show_back():  
    card_canvas.itemconfig(card_id, image=back_card_image)
    language = list(current_card.keys())[1]
    card_canvas.itemconfig(language_label, text=language, fill="white")
    card_canvas.itemconfig(word_label, text=current_card[language], fill="white")

def score_correct():
    word_list.remove(current_card)
    next_card()
       
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=PADDING, pady=PADDING, bg = BACKGROUND_COLOR)

front_card_image = tkinter.PhotoImage(file="images/card_front.png")
back_card_image = tkinter.PhotoImage(file="images/card_back.png")
card_canvas = tkinter.Canvas(height=CARD_HEIGHT, width=CARD_WIDTH, 
    bg=BACKGROUND_COLOR, highlightthickness=0)
card_id = card_canvas.create_image(CARD_WIDTH/2, CARD_HEIGHT/2, image=front_card_image)
language_label = card_canvas.create_text(LANGUAGE_LOCATION_X, LANGUAGE_LOCATION_Y,
    text="Title", font=LANGUAGE_FONT)
word_label = card_canvas.create_text(WORD_LOCATION_X, WORD_LOCATION_Y,
    text="Word", font=WORD_FONT)
card_canvas.grid(row=0, column=0, columnspan=2)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0,
    command=next_card)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, 
    command=score_correct)
right_button.grid(row=1, column=1)

timer = window.after(1000, show_back)
next_card()
window.mainloop()

data_frame = pandas.DataFrame.from_dict(word_list)
data_frame.to_csv("data/words_to_learn.csv", index=False)