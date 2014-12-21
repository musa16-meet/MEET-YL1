import turtle
turtle.ht()
turtle.tracer(0,1)
turtle.getscreen().listen()
color="black"
def square (x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    turtle.end_fill()

def circle (x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.pencolor(color)
    turtle.dot(50)

def change_colortored():
    turtle.pencolor("red")
    color="red"
def change_color_to_blue():
    turtle.pencolor("blue")
    color="blue"
def change_colortoyellow():
    turtle.pencolor("yellow")
    color="yellow"
def change_colortogreen():
    turtle.pencolor("green")
    color="green"
def clear ():
    turtle.clear()

turtle.onclick(square,btn =1,add=True)
turtle.onscreenclick(square,btn =1,add = True)
turtle.ondrag(square,btn =1,add=True)
    
turtle.onclick(circle,btn =3,add=True)
turtle.onscreenclick(circle,btn =3,add = True)
turtle.ondrag(circle,btn =3,add=True)

turtle.getscreen().onkey(clear,"c")
turtle.getscreen().onkey(change_colortored,"r")
turtle.getscreen().onkey(change_color_to_blue,"b")
turtle.getscreen().onkey(change_colortoyellow,"y")
turtle.getscreen().onkey(change_colortogreen,"g")

turtle.listen()
turtle.mainloop()
