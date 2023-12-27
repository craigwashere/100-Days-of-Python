import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PADDING = 20
QUESTION_FONT = ("Arial", 20, "italic")
QUESTION_HEIGHT = 300
QUESTION_WIDTH = 250

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=PADDING, pady=PADDING)
        self.score_label = tkinter.Label(text=f'Score: {self.quiz.score}',
                                         fg="white",
                                         bg=THEME_COLOR, 
                                         font=("Arial", 10, "italic"))
        self.score_label.grid(row=0, column = 1)
        
        self.question_canvas = tkinter.Canvas(height=QUESTION_HEIGHT,
                                              width=QUESTION_WIDTH, 
                                              highlightthickness=0)
        self.question_label = self.question_canvas.create_text(QUESTION_WIDTH/2,QUESTION_HEIGHT/2, 
                text="Title", font=QUESTION_FONT, width=QUESTION_WIDTH-20)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.question_canvas.itemconfig(self.question_label, 
                text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_label, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def give_feedback(self,is_right):
        if is_right:
            color = "green"
        else:
            color = "red"
        self.question_canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)
    
    def draw_score(self):
        self.score_label.config(text=f'Score: {self.quiz.score}')
        
    def check_answer_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)
        if is_correct:
            self.draw_score()
        self.get_next_question()
            
    def check_answer_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
        if is_correct:
            self.draw_score()
        self.get_next_question()
        