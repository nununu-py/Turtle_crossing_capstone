from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.list_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        rand_number = random.randint(1, 4)
        if rand_number == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            random_y = random.randint(-250, 230)
            car.goto(300, random_y)
            self.list_cars.append(car)

    def move_cars(self):
        for cars in self.list_cars:
            cars.forward(self.cars_speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT
