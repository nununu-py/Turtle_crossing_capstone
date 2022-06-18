from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)
