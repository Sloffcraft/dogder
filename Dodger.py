import turtle

win = turtle.Screen()
win.title("Dogder")
win.bgcolor("black")
win.setup(width = 1000, height = 600)
win.tracer()

#Main player
pl = turtle.Turtle()
pl.shape("square")
pl.color("white")
pl.penup()
pl.speed(0)
pl.goto(-450,0)

#obticles
ob = turtle.Turtle()
ob.shape("square")
ob.shapesize(stretch_wid = 8 , stretch_len = 1)
ob.color("white")
ob.speed(0)
ob.penup()
ob.goto(-400,0)
ob.dy = 5

#goal 
go = turtle.Turtle()
go.shape("triangle")
go.color("white")
go.speed(0)
go.penup()
go.goto(450,0)

#functions
def pl_right():
    x = pl.xcor()
    x += 20
    pl.setx(x)
    
def pl_up():
	y = pl.ycor()
	y += 20
	pl.sety(y)

def pl_down():
	y = pl.ycor()
	y -= 20
	pl.sety(y)
	
#keyboard binding
win.listen()
win.onkeypress(pl_right , "d")
win.onkeypress(pl_up , "w")
win.onkeypress(pl_down , "s")

#Main game loop
while True:
    win.update()
    
    #obticles movement 
    ob.sety(ob.ycor() + ob.dy)
    
    if ob.ycor() > 250:
        ob.sety(250)
        ob.dy *= -1
        
    if ob.ycor() < -250:
        ob.sety(-250)
        ob.dy *= -1
       
   #corride with the main player 
          
    if pl.xcor() > 400 and (pl.ycor() > ob.ycor + 50) and (pl.ycor > ob.ycor - 50 ):
        pl.goto(-450,0)