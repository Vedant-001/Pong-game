import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by VK")
wn.bgcolor("black")
wn.setup(width = 800, height = 600) #(0,0) is at the center
wn.tracer(0)


#Score
scoreA,scoreB = 0,0


#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0) #Speed of animation (0 is fastest)
paddleA.shape("square") #default is 20px X 20px
paddleA.color("white")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350,0) 

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0) #Speed of animation (0 is fastest)
paddleB.shape("square") #default is 20px X 20px
paddleB.color("white")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(4)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
#ball moves by 0.1 pixels everytime
ball.dx = 0.1
ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0    Player B: 0", align = "center", font = ("Times New Roman",24,"bold"))

#Functions for movements

def paddleA_up():
	y = paddleA.ycor() #y-coordinate of the paddle
	y += 20
	paddleA.sety(y)

def paddleA_down():
	y = paddleA.ycor()
	y -= 20
	paddleA.sety(y)

def paddleB_up():
	y = paddleB.ycor() #y-coordinate of the paddle
	y += 20
	paddleB.sety(y)

def paddleB_down():
	y = paddleB.ycor()
	y -= 20
	paddleB.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddleA_up,"w")
wn.onkeypress(paddleA_down,"s")
wn.onkeypress(paddleB_up,"Up")
wn.onkeypress(paddleB_down,"Down")

# Main Game loop
while True:
	wn.update() #updates the screen

	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border check
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("bounce.mp3",winsound.SND_ASYNC)

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("bounce.mp3",winsound.SND_ASYNC)

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		scoreA += 1
		pen.clear()
		pen.write("Player A: {}    Player B: {}".format(scoreA,scoreB), align = "center", font = ("Times New Roman",24,"bold"))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		scoreB += 1
		pen.clear()
		pen.write("Player A: {}    Player B: {}".format(scoreA,scoreB), align = "center", font = ("Times New Roman",24,"bold"))

	#Paddle-ball collision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor()+40) and (ball.ycor() > paddleB.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("boing.mp3",winsound.SND_ASYNC)

	if (ball.xcor() < - 340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor()+40) and (ball.ycor() > paddleA.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("boing.mp3",winsound.SND_ASYNC)