# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

import tkinter as tk
import random
import time
import threading
import datetime

class WPM(tk.Frame):
    def get_new_word(self):
        self.target_word = random.choice(self.word_list)
        self.target.config(text = self.target_word)
        self.submit.delete(0, 'end')
        self.time_at_start_of_typing = datetime.datetime.now()

    def adjust_scores(self, value):
        self.total_words_typed += 1
        time_to_type_word = self.time_at_end_of_typing - self.time_at_start_of_typing
        self.total_typing_time += time_to_type_word
        if value == self.target_word:
            self.correct_words_typed += 1
            self.words_per_minute = int((self.correct_words_typed/self.total_typing_time.total_seconds())*60)
        self.accuracy_label.config(text = "Accuracy: {:02f}".format((self.correct_words_typed/self.total_words_typed)*100))
        self.WPM_label.config(text = "WPM: {:02d}".format(self.words_per_minute))

    def OnEntryClick(self, event):
        value = self.sv.get().strip()
        changed = True if self.prevlaue != value else False
        if changed:
            if len(value) >= len(self.target_word):
                self.time_at_end_of_typing = datetime.datetime.now()
                self.adjust_scores(value)
                self.get_new_word()
        prevlaue = value

    def init_variables(self):
        self.words_per_minute = 0
        self.elapsed_time = 0
        self.accuracy = 0
        self.target_word = random.choice(self.word_list)
        self.prevlaue=''
        self.total_words_typed = 0
        self.correct_words_typed = 0
        self.start_time = datetime.timedelta.min
        self.timer = threading.Thread(target=self.Start2)
        self.testing = False
        self.total_typing_time = datetime.timedelta()
    
    def Stop(self):
        self.init_variables()
        self.start_button["state"] = tk.NORMAL
        self.target.config(text = "Press Start")
        self.submit["state"] = tk.DISABLED
        
    def Reset(self):
        self.Stop()
        self.WPM_label.config(text = "WPM: 0")
        self.time_label.config(text = "Time: 00:00")
        self.accuracy_label.config(text = "Accuracy: --")
        
    def Start2(self):
        while self.testing == True:
            sec = (datetime.datetime.now() - self.start_time).seconds
            mins = sec // 60
            mins = mins % 60
            sec = sec % 60
            self.time_label.config(text = "Time: {0:02d}:{1:02d}".format(mins, sec))
            time.sleep(1)

    def Start(self):
        self.start_button["state"] = tk.DISABLED
        self.submit["state"] = tk.NORMAL
        self.start_time = datetime.datetime.now()
        self.testing = True
        self.get_new_word()
        self.timer.start()
        self.submit.focus_set()

    def __init__(self, the_window):
        tk.Frame.__init__(self, the_window)
        
        with open('master_list.txt', 'r') as word_file:
            self.word_list = [word.lower() for word in word_file.read().split()]

        self.init_variables()
        #canvas = tk.Canvas(root, height=600, width=600, bg='white')
        #canvas.pack(fill=tk.BOTH, expand=True)

        # this will create a label widget
        self.WPM_label = tk.Label(self, text = f"WPM: 0")
        self.time_label = tk.Label(self, text = f"Time: 00:00")

        # grid method to arrange labels in respective
        # rows and columns as specified
        self.WPM_label.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
        self.time_label.grid(row = 0, column = 1, sticky = tk.W, pady = 2)

        self.accuracy_label = tk.Label(self, text = f"Accuracy: --")
        self.accuracy_label.grid(row = 1, column = 0, columnspan=2, sticky = tk.W, pady = 2)

        # entry widgets, used to take entry from user
        self.target = tk.Label(self, text = "Press Start")

        self.sv = tk.StringVar()
        self.submit = tk.Entry(self, textvariable = self.sv)
        self.submit.bind("<KeyRelease>", self.OnEntryClick)
        self.submit["state"] = tk.DISABLED
        
        # this will arrange entry widgets
        self.target.grid(row = 2, column = 0, columnspan=2, pady = 2)
        self.submit.grid(row = 3, column = 0, columnspan=2, pady = 2)

        # button widget
        self.start_button = tk.Button(self, text = "Start", command=self.Start)
        self.reset_button = tk.Button(self, text = "Reset", command=self.Reset)
        self.stop_button  = tk.Button(self, text = "Stop", command=self.Stop)
        
        # arranging button widgets
        self.start_button.grid(row = 4, column = 0, sticky = tk.W)
        self.reset_button.grid(row = 4, column = 1, sticky = tk.W)
        self.stop_button.grid(row=4, column=1, sticky=tk.E)

# creating main tkinter window/toplevel
root = tk.Tk()

frameA = WPM(root)
frameA.grid(row=0, column=0)
# infinite loop which can be terminated
# by keyboard or mouse interrupt
root.mainloop()
