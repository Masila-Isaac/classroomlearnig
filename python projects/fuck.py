
from turtle import *
import turtle

Screen().bgcolor((1,1,1))
screenx, screeny = 650, 1050
turtle.title("FUCK YOU !!!!!!")
turtle.setup(screenx, screeny)
t= Turtle() 
t.pencolor('red') 
t.speed(10)
t.begin_fill() 
# start filling 
for i in range(1): 
    t.color((0,0,0), (0.909803922, 0.745098039, 0.674509804)) 
    t.left(90) 
    t.forward (80) 
    t.right(90)
    t.circle(80, 90) 
    t.forward(160) 
    t.circle(40, 180) 
    t.right(180) 
    t.circle(40, 180) 
    t.right(180) 
    t.forward(160) 
    t.circle(40,180)  
    t.forward(160) 
    t.right(180) 
    t.circle(40,180)  
    t.forward(160)  
    t.right(180) 
    t.penup() 
    t.forward(80) 
    t.pendown() 
    t.circle(40,180) 
    t.left(50) 
    t.forward(100) 
    t.right(50) 
    t.write("FUCK U !!!", font=( 
      "Verdana", 40, "bold")) 
    t.circle(80,90) 
    t.right(90) 
    t.forward(80)  
    t.left(90)
    t.forward(180) 
    t.pendown()  
t.end_fill() 
    # end filling
done()
