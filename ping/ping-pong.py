import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.bgcolor("black")
window.bgpic('imag.gif')
window.setup(width=800, height=600)
window.tracer(0)

#Paddle_1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

#Paddle_2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)

#score
score_1 = 0
score_2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("red")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))

ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2
def paddle_1_up():
    y = paddle_1.ycor()
    y+=20
    paddle_1.sety(y)
def paddle_1_down():
    y = paddle_1.ycor()
    y-=20
    paddle_1.sety(y)
def paddle_2_up():
    y = paddle_2.ycor()
    y+=20
    paddle_2.sety(y)
def paddle_2_down():
    y = paddle_2.ycor()
    y-=20
    paddle_2.sety(y)



#keyboard
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")
# main loop
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0, 0)
        ball.dx*=-1
        score_1 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))
    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx*=-1
        score_2 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))

    #collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    
