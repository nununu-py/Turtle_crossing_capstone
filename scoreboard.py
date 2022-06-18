from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=-150, y=265)
        self.write(arg=f"Score : {self.level}", move=False, align="center", font=FONT)

    def add_score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Score : {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
