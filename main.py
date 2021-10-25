import time
from turtle import Screen
from paddle import Paddle
from score import ScoreBoard
from ball import Ball

screen_x = 768
screen_y = 480

x_lim=screen_x/2-20
y_lim=screen_y/2-20

screen = Screen()
screen.setup(screen_x, screen_y)
screen.bgcolor("black")
screen.title("Pong")

p1 = Paddle()
p1.set(-x_lim+10)
p2 = Paddle()
p2.set(x_lim-20)

screen.listen()
if p1.ycor()<y_lim:
    screen.onkey(p1.up,"w")
if -p1.ycor()<y_lim:
    screen.onkey(p1.down,"s")
if p2.ycor()<y_lim:
    screen.onkey(p2.up,"Up")
if -p2.ycor()<y_lim:
    screen.onkey(p2.down,"Down")
ball= Ball()
line = ScoreBoard(screen_y)
line.draw_line()
score =ScoreBoard(screen_y)
score.draw_score()

game_on=True

while game_on:
    ball.move()
    x=ball.xcor()
    y=ball.ycor()
    if abs(y) > y_lim:
        ball.reflect_wall()
    if p1.distance(ball)<30 and abs(x)>x_lim-20 and abs(x)<x_lim-10:
        ball.reflect_p1()
    if p2.distance(ball)<30 and abs(x)>x_lim-30 and abs(x)<x_lim-20:
        ball.reflect_p2()
    if abs(x)> screen_x/2+30:
        if x >0:
            score.score_p1()
        else:
            score.score_p2()
        time.sleep(1)
        ball.respawn()

screen.exitonclick()
