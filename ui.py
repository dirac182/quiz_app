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
        self.true_button = Button(image=self.true_img,command=self.true_press)
        self.false_button = Button(image=self.false_img,command=self.false_press)
        self.true_button.grid(column=0,row=2,padx=20,pady=20)
        self.false_button.grid(column=1,row=2,padx=20,pady=20)
        self.score = Label(text="",bg=THEME_COLOR,fg="white",font=("arial",12,"bold"))
        self.score.grid(column=1,row=0,padx=20,pady=20)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You have reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_press(self):
        answer = self.quiz.check_answer("true")
        self.give_feedback(answer)
    def false_press(self):
        answer = self.quiz.check_answer("false")
        self.give_feedback(answer)

    def give_feedback(self,answer):
        if answer:
            self.canvas.config(bg="green")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.canvas.config(bg="red")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.window.after(1000, self.get_question)


