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
        with open("data.txt") as data :
            self.hihg_score=int(data.read())
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score :{self.hihg_score}  ", True, align=ALIGNENT, font=FONT)
    def reset(self):
        if self.score>self.hihg_score:
            self.hihg_score=self.score
            with open("data.txt",mode="w") as data :
                data.write(f"{self.hihg_score}")
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", True, align=ALIGNENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(0,270)
        self.update_score()