# Python program demonstrating
# ScrolledText widget in tkinter
# https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/?ref=gcse


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def keyDown(event):
    global text_area, erase_timer
    last_char_visible= text_area.bbox("end-1c")
    if last_char_visible:
        text_area.see("end")
    
    if not erase_timer is None:
        win.after_cancel(erase_timer)
        erase_timer = None
    
        
def keyUp(event):
    global erase_timer
    if erase_timer is None:
        erase_timer = win.after(5000, erase_text)
        
        
def erase_text():
    global text_area
    text_area.delete('1.0', tk.END)
    
# Creating tkinter main window
win = tk.Tk()
win.title("ScrolledText Widget")

# Title Label
ttk.Label(win, text = "Most Dangerous Writing App",
		font = ("Times New Roman", 15),
		background = 'green',
		foreground = "white").grid(column = 0, row = 0)

# Creating scrolled text
# area widget
text_area = scrolledtext.ScrolledText(win,
									wrap = tk.WORD,
									width = 40,
									height = 10,
									font = ("Times New Roman", 15))

text_area.grid(column = 0, pady = 10, padx = 10)
text_area.bind("<KeyPress>", keyDown)
text_area.bind("<KeyRelease>", keyUp)

erase_timer = None

# Placing cursor in the text area
text_area.focus()
win.mainloop()
