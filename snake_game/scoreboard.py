from turtle import  Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.write(f"Score:{self.score}  ", True, align="center",font=('Arial', 18, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(0,270)
        self.write(f"Score:{self.score}  ", True, align="center",font=('Arial', 18, 'normal'))