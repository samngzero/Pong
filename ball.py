from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speedfactor=0
        self.speed_coefficient=0.3
        self.speed(0)
        self.shape("circle")
        self.respawn()
        self.showturtle()
        self.setheading(randint(-30, 30) + (180 ** randint(0, 1)))


    def respawn(self):
        self.speedfactor=0
        self.goto(0, randint(-100, 100))
        self.setheading(self.heading()+180 +randint(-30, 30))


    def move(self):
        self.fd(4+self.speed_coefficient*self.speedfactor)

    def reflect_wall(self):
        self.setheading(-self.heading())
        self.speedfactor+=1

    def reflect_p1(self):
        self.setheading(self.heading() + 90 +randint(0,10)*(-1)**randint(0,1))
        self.speedfactor += 1

    def reflect_p2(self):
        self.setheading(self.heading() - 90 +randint(0,10)*(-1)**randint(0,1))
        self.speedfactor += 1
