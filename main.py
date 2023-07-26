import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")


car.car_create()
score.score_board()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    car.car_move()
    car.car_continue()

    for i in car.segments:
        if player.distance(i) < 23:
            score.game_over()
            game_is_on = False


    if player.ycor() == 280:
        player.goto(0, -280)
        car.a += 1
        score.level_up()

screen.exitonclick()

