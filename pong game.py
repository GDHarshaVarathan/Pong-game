from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
screen=Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(width=800,height=800)
screen.tracer(0)
paddle1=Paddle((-350,0))
paddle2=Paddle((350,0))
ball=Ball()
screen.listen()
screen.onkey(paddle1.move_up,"w")
screen.onkey(paddle1.move_down,"s")
screen.onkey(paddle2.move_up,"Up")
screen.onkey(paddle2.move_down,"Down")
penny=Turtle()
penny.hideturtle()
penny.speed("fastest")
penny.color("white")
penny.penup()
penny.goto(0,400)
penny.setheading(270)
while penny.ycor()>=-400:
    penny.pendown()
    penny.forward(10)
    penny.penup()
    penny.forward(10)
    penny.pendown()
penny1=Turtle()
penny1.hideturtle()
penny1.speed("fastest")
penny1.color("white")
global left_score
global right_score
left_score=0
right_score=0
def l_score():
    global left_score
    left_score+=1
def r_score():
    global right_score
    right_score+=1
def update_scoreboard():
    penny1.clear()
    penny1.penup()
    penny1.goto(-100,250)
    penny1.write(f"{left_score}",align="center",font=("Courier",80,"normal"))
    penny1.penup()
    penny1.goto(100,250)
    penny1.write(f"{right_score}",align="center",font=("Courier",80,"normal"))
is_on=True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()
    update_scoreboard()
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce()
    if ball.distance(paddle2)<50 and ball.xcor()>320 or ball.distance(paddle1)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor() > 390:
        l_score()
        update_scoreboard()
        ball.goto(0,0)
        ball.move_speed=0.1
    if ball.xcor() < -390:
        r_score()
        update_scoreboard()
        ball.goto(0,0)
        ball.move_speed=0.1





