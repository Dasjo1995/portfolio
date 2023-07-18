from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from blocks import Blocks

screen = Screen()
screen.bgcolor("purple")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle((0, -270))
ball = Ball()
blocks = Blocks()

screen.listen()
screen.onkey(paddle.go_right, "a")
screen.onkey(paddle.go_left, "d")


game_is_on = True
while game_is_on:


    # ----------------------------- Ball Section -------------------------------------------------
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_y()
        ball.move_speed -= 0.01

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    #Detect paddle misses
    if ball.ycor() < -280:
        ball.reset_position()

    # ----------------------------- Block Section -------------------------------------------------

    for block in blocks.list:
        if ball.distance(block) < 50 and ball.ycor() > 210:
            ball.bounce_y()
            block.hideturtle()
            blocks.list.remove(block)
            if len(blocks.list) == 0:
                print("game over")
                victory = Turtle()
                victory.hideturtle()
                victory.goto(0, 0)
                victory.write("Victory!", font=("Helvetica", 50, "normal"))





screen.exitonclick()

