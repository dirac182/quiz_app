from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.title("Quizzler")
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.canvas = Canvas(height=250,width=300,bg="white",highlightthickness=0)
        self.question = self.canvas.create_text(150,125,text="Question Goes Here",font=("arial",20,"italic"),fill=THEME_COLOR,width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)
        self.true_button = Button(image=self.true_img)
        self.false_button = Button(image=self.false_img)
        self.true_button.grid(column=0,row=2,padx=20,pady=20)
        self.false_button.grid(column=1,row=2,padx=20,pady=20)
        self.score = Label(text="Score: 0",bg=THEME_COLOR,fg="white",font=("arial",12,"bold"))
        self.score.grid(column=1,row=0,padx=20,pady=20)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question,text=q_text)