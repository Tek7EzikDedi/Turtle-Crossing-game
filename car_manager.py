from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.segments = []
        self.a = 1


    def car_create (self):
        for i in range(random.randint(15, 20)):
            i = Turtle()
            i.shape("square")
            i.penup()
            i.color(random.choice(COLORS))
            i.shapesize(1, 2)
            posıtıon = (random.randint(300, 1000), random.randint(-220, 300))
            i.goto(posıtıon)
            self.segments.append(i)

    def car_create_one (self):
        i = Turtle()
        i.shape("square")
        i.penup()
        i.color(random.choice(COLORS))
        i.shapesize(1, 2)
        posıtıon = (random.randint(300, 1000), random.randint(-220, 300))
        i.goto(posıtıon)
        self.segments.append(i)


    def car_continue(self):
        for i in self.segments:
            if i.xcor() < -320:
                i.goto(0, 400)
                self.segments.remove(i)
                self.car_create_one()



    def car_move(self):
        for i in self.segments:
            new_x = i.xcor()
            new_y = i.ycor()
            i.goto(new_x - self.a, new_y)