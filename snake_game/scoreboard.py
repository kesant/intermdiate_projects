from turtle import  Turtle
ALIGNENT="center"
FONT=('Arial', 20, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.write(f"Score:{self.score}  ", True, align=ALIGNENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(0,270)
        self.update_score()