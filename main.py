from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()

### Create the screen
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

### Create paddle
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

### Move a paddle
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "s")
screen.onkey(l_paddle.down, "w")

### Create the ball and make it move
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    ### Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_move_y()

    ### Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()  > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_move_x()
    ### Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()


    ### Detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()