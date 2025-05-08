import turtle 
tortuga=turtle.Turtle()

def LetraD(ancho:int, color:str, forma:str):
    
    tortuga.pensize(ancho)
    tortuga.color(color)
    tortuga.begin_fill()
    tortuga.shape(forma)
    tortuga.penup()
    tortuga.goto(-450, 0)
    tortuga.pendown()
    tortuga.circle(100,180)  
    tortuga.rt(90) 
    tortuga.bk(200) 
    tortuga.end_fill()
    tortuga.penup()
    tortuga.goto(-330, 0)
    tortuga.pendown()
    tortuga.rt(15)
    tortuga.fd(200) #fd, bk 
    tortuga.lt(210)
    tortuga.fd(200)
    tortuga.penup()
    tortuga.goto(-300, 100)
    tortuga.pendown()
    tortuga.rt(-80)
    tortuga.fd(50)
    tortuga.penup()
    tortuga.goto(-200, 0)
    tortuga.pendown()
    tortuga.rt(-85)
    tortuga.fd(200)
    tortuga.rt(160)
    tortuga.fd(210)
    tortuga.rt(200)
    tortuga.fd(200)
    # i
    tortuga.penup()
    tortuga.goto(-100, 0)
    tortuga.pendown()
    tortuga.fd(200)
    # punto i
    tortuga.penup()
    tortuga.goto(-100, 220)
    tortuga.pendown()
    tortuga.fd(5)
    # e
    tortuga.penup()
    tortuga.goto(-70, 0)
    tortuga.pendown()
    tortuga.fd(200)
    tortuga.rt(90)
    tortuga.fd(50)
    tortuga.penup()
    tortuga.goto(-70, 100)
    tortuga.pendown()
    tortuga.rt(360)
    tortuga.fd(50)
    tortuga.penup()
    tortuga.goto(-70, 0)
    tortuga.pendown()
    tortuga.rt(0)
    tortuga.fd(50)
    #l
    tortuga.penup()
    tortuga.goto(0, 0)
    tortuga.pendown()
    tortuga.rt(0)
    tortuga.fd(50)
    tortuga.penup()
    tortuga.goto(0, 200)
    tortuga.pendown()
    tortuga.rt(90)
    tortuga.fd(200)
    turtle.done()



def emoji():
    screen = turtle.Screen()
    screen.bgcolor("white")  
    
    
    tortuga = turtle.Turtle()
    tortuga.speed(5) 
    tortuga.pensize(3)
    tortuga.shape("turtle")

    # Cara 
    tortuga.penup()
    tortuga.goto(200, 50) # 0 -100
    tortuga.pendown()
    tortuga.color("yellow", "#FFFF00")  # Borde amarillo, relleno amarillo claro
    tortuga.begin_fill()
    tortuga.circle(100)  # Círculo principal
    tortuga.end_fill()

    # --- Ojos ---
    # Ojo izquierdo
    tortuga.penup()
    tortuga.goto(220, 180)
    tortuga.pendown()
    tortuga.color("black")
    tortuga.begin_fill()
    tortuga.circle(15)
    tortuga.end_fill()

    # Ojo derecho
    tortuga.penup()
    tortuga.goto(180, 180)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.circle(15)
    tortuga.end_fill()

    # Boca 
    tortuga.penup()
    tortuga.goto(155, 140)
    tortuga.pendown()
    tortuga.color("black")
    tortuga.setheading(-60)  
    tortuga.circle(50, 120)  

   

emoji()    
LetraD(15,"purple","turtle")  