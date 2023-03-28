import turtle

screen = turtle.Screen()
screen.bgcolor("#05192D")
screen.setup(width=550, height=370)
screen.title("Drawing the Root Academic Logo")

my_turtle = turtle.Turtle()
my_turtle.pensize(7)
my_turtle.shape("turtle")


my_turtle.penup()
my_turtle.backward(100)
my_turtle.pendown()

# the vertical line (main line)
my_turtle.pencolor("#FFFFFF")
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(150)
my_turtle.forward(115)
my_turtle.left(130)
my_turtle.forward(110)
my_turtle.right(140)
my_turtle.forward(110)
my_turtle.penup()
my_turtle.goto(-100,100)
my_turtle.pendown()

my_turtle.pencolor("#03EF62")
my_turtle.setheading(0)
my_turtle.penup()
my_turtle.forward(15)
my_turtle.pendown()
my_turtle.forward(45)
my_turtle.right(120)
my_turtle.forward(45)

my_turtle.penup()
my_turtle.goto(-15,40)
my_turtle.pendown()
my_turtle.setheading(0)
my_turtle.forward(20)

my_turtle.penup()
my_turtle.goto(-20,30)
my_turtle.pendown()
my_turtle.setheading(0)
my_turtle.forward(30)

my_turtle.hideturtle()

#%%
