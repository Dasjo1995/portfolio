import time
from turtle import Screen, Turtle
from ship import Ship
from aliens import Aliens
from shoot import Shoot

screen = Screen()
screen.bgcolor("purple")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

ship = Ship((0, -270))
aliens = Aliens()

list = []

def shots():
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("circle")
    new_turtle.penup()
    new_turtle.hideturtle()
    print(new_turtle)
    new_turtle.goto(ship.xcor(), ship.ycor())
    list.append(new_turtle)

def move_aliens():
    for alien in aliens.list:
        p = alien.pos()
        alien_x = p[0]
        alien_y = p[1]
        new_y = alien_y - 0.1
        alien.goto(alien_x, new_y)
        if p[1] < -200:
            defeat = Turtle()
            defeat.hideturtle()
            defeat.penup()
            defeat.goto(-100, 0)
            defeat.write("Defeat", font=("Helvetica", 50, "normal"))
            game_is_on = False


screen.listen()
screen.onkey(ship.go_right, "a")
screen.onkey(ship.go_left, "d")
screen.onkey(shots, "w")

y_move = 1

game_is_on = True
while game_is_on:
    screen.update()
    for shot in list:
        shot.showturtle()
        new_y = shot.ycor() + y_move
        shot.goto(shot.xcor(), new_y)
        if shot.ycor() > 300:
            shot.hideturtle()
            list.remove(shot)

    #shoot.move(ship.xcor(), ship.ycor())
        for alien in aliens.list:
            if shot.distance(alien) < 50:
                alien.hideturtle()
                aliens.list.remove(alien)
                if len(aliens.list) == 0:
                    print("game over")
                    victory = Turtle()
                    victory.hideturtle()
                    victory.penup()
                    victory.goto(-100, 0)
                    victory.write("Victory!", font=("Helvetica", 50, "normal"))

    for alien in aliens.list:
        for shot in list:
            if shot.distance(alien) < 40:
                shot.hideturtle()
                list.remove(shot)
                alien.hideturtle()
                aliens.list.remove(alien)

    move_aliens()

screen.exitonclick()
