import tkinter
# ---------------------------- CONSTANTS ----------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET --------------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ----------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    # work_seconds = WORK_MIN * 60
    # short_break_seconds = SHORT_BREAK_MIN * 60
    # long_break_seconds = LONG_BREAK_MIN * 60
    long_break_seconds = 10
    short_break_seconds = 5
    work_seconds = 3
    
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def format_time(count):
    minutes = str(int(count/60)).zfill(2)
    seconds = str(int(count%60)).zfill(2)
    
    return f"{minutes}:{seconds}"
    
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=format_time(count))
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_label.config(text="✔"*(int(reps/2)))
        
# ---------------------------- UI SETUP ------------------------------------------ #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
check_label.grid(row=3, column=1)

window.mainloop()