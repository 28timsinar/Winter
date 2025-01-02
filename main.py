import turtle
t = turtle.Turtle()
t_ground = turtle.Turtle()
t.hideturtle()
t_ground.hideturtle()
t.speed(0)

t_ground.speed(0)
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("steel blue")
t.pensize(1)
#ground

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.fillcolor("white")
t_ground.pencolor("cornflower blue")
t_ground.begin_fill()
t_ground.goto(-1000,-100)
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()
#end ground

t.penup()
t_ground.pendown()


#Snowman 1

t.pencolor("blue")
t.fillcolor('white')
t.penup()
#3rd tier
t.goto(-150,-100)
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()
t.penup()

#2nd tier

t.end_fill()
t.goto(-150,-1)
t.begin_fill()
t.pendown()
t.circle(35)
t.end_fill()
t.penup()

#1st tier

t.end_fill()
t.goto(-150,68)
t.begin_fill()
t.pendown()
t.circle(25)
t.end_fill()
t.penup()

#buttons
t.pencolor("brown")
t.fillcolor('brown')
t.penup()

t.end_fill()
t.goto(-150,-30)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()
t.penup()

t.end_fill()
t.goto(-150,-11)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()
t.penup()

t.end_fill()
t.goto(-150,7)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()
t.penup()

#eyes
t.pencolor("black")
t.fillcolor('black')
t.penup()

t.end_fill()
t.goto(-160,100)
t.begin_fill()
t.pendown()
t.circle(3)
t.end_fill()
t.penup()

t.end_fill()
t.goto(-140,100)
t.begin_fill()
t.pendown()
t.circle(3)
t.end_fill()
t.penup()

#nose
t.penup()
t.goto(-152,100)
t.pendown()

t.fillcolor("orange")
t.begin_fill()
t.goto(-152,90)
t.goto(-110,90)
t.goto(-152,100)
t.end_fill()
t.penup()

#mouth
t.goto(-152, 80)
t.dot()
t.penup()


t.goto(-145, 80)
t.pendown()
t.dot()
t.penup()


t.goto(-159, 82)
t.pendown()
t.dot()
t.penup()

#arms
t.pensize(3)
t.pencolor("brown")
t.goto(-120, 40)
t.pendown()
t.goto(-90, -30)
t.penup()

t.goto(-180,40)
t.pendown()
t.goto(-230,-30)
t.penup()
t.pensize(1)
#present
t.pencolor("dark red")
t.fillcolor("red")
t.goto(-50,-100)
t.begin_fill()
t.pendown()
t.goto(-50,-50)
t.goto(0,-50)
t.goto(0,-100)
t.goto(-50,-100)
t.end_fill()
t.penup()

t.pencolor("dark green")
t.fillcolor("green")

t.goto(-30,-50)
t.begin_fill()
t.pendown()
t.circle(7)
t.penup()
t.goto(-20,-50)
t.pendown()
t.circle(7)
t.end_fill()
t.penup()



#tree
t.pencolor("black")
t.fillcolor("brown")
t.begin_fill()
t.goto(10,-100)
t.pendown()
t.goto(10,-20)
t.goto(30,-20)
t.goto(30,-100)
t.goto(10,-100)
t.end_fill()
t.penup()

t.fillcolor("green")
t.begin_fill()
t.goto(-40, -20)
t.pendown()
t.goto(80,-20)
t.goto(20, 150)
t.goto(-40, -20)
t.end_fill()
t.penup()

#snowflake
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.goto(-50, 140)
t.pendown()
t.circle(20)
t.end_fill()
t.penup()


t.pencolor("white")
t.goto(-50,135)
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()

t.penup()
t.goto(-50,175)
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()

t.penup()
t.goto(-70,150)
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()

t.penup()
t.goto(-32,150)
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()
t.penup()

t.pencolor("steel blue")
t.fillcolor("steel blue")
t.goto(-50,150)
t.begin_fill()
t.pendown()
t.circle(10)
t.end_fill()
t.penup()

t.pencolor("gold")

#ornament
t.goto(20,30)
t.pendown()
t.fillcolor("hot pink")
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.goto(20,60)
t.pencolor("gold")
t.pendown()
t.dot(5)
t.penup()


t.goto(20,45)
t.dot()
t.penup()
t.goto(10,45)
t.dot()
t.penup()
t.goto(30,45)
t.dot()
t.penup()

#tent thing
t.pencolor("black")

t.pensize(2)
t.penup()
t.goto(-300,230)
t.pendown()
t.goto(310,230)
t.penup()

t.pensize(10)
t.pencolor("brown")
t.goto(-300,230)
t.pendown()
t.goto(-300,-100)
t.penup()

t.goto(310,230)

t.pendown()
t.goto(310,-100)
t.penup()

t.pencolor("red")
t.goto(-290, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(-260, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(-230, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(-200, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(-170, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(-140, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(-110, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(-80, 225)
t.dot()
t.penup()


t.pencolor("red")
t.goto(-50, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(-20, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(10, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(40, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(70, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(100, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(130, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(160, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(190, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(220, 225)
t.dot()
t.penup()

t.pencolor("red")
t.goto(250, 225)
t.dot()
t.penup()

t.pencolor("green")
t.goto(280, 225)
t.dot()
t.penup()



t.pensize(1)
t.pencolor("dark red")

t.goto(140,150)
t.write("Happy Holidays!",font=("arial",20,'bold'),align="center")

#gingerbread house
t.penup()
t.pencolor("white")
t.pensize(2)
t.fillcolor("brown")
t.goto(130,-100)
t.pendown()
t.begin_fill()
t.goto(130,0)
t.goto(250,0)
t.goto(250,-100)
t.goto(130,-100)
t.end_fill()
t.penup()

t.goto(130,0)
t.pendown()
t.begin_fill()
t.goto(190,100)
t.goto(250,0)
t.goto(130,0)
t.end_fill()
t.penup()
t.pensize(1)
t.pencolor("red")

t.goto(190,-50)
t.pendown()
t.circle(20)
t.penup()
t.goto(190,-30)
t.pensize(50)
t.pendown()
t.goto(190,-70)
t.penup()


#wreath
t.pencolor("white")
t.goto(190, 10)
t.fillcolor("green")
t.pensize(1)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()

t.fillcolor("brown")
t.goto(190,25)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.pencolor("red")
t.goto(200,25)
t.dot()
t.penup()

t.goto(180,20)
t.dot()
t.penup()

t.goto(183,60)
t.dot()
t.penup()

t.goto(200,60)
t.dot()
t.penup()

t.goto(208,40)
t.dot()
t.penup()

t.goto(170,40)
t.dot()
t.penup()










t.dot()
turtle.done()