import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
the_obstacle = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="w")
screen.onkey(fun=player.move_backward, key="s")

game_is_on = True
while game_is_on:
    the_obstacle.make_car()
    the_obstacle.move_cars()

    for cars in the_obstacle.list_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 240:
        player.goto(0, -280)
        score.add_score()
        the_obstacle.increase_speed()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
