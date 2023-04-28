import turtle
import math
import time
turtle.speed(0)
t = turtle.Turtle()
#variables
pen_color = str()
fill_color = str()
pen_size = int()
size = int()
#global variables for circles functions
horizontal = int()
radius = int()
locations = ['bank', 'breakfast']
t.reset() #reset turtle
t.shape('turtle')#make our turtle
t.pencolor('green')
t.pensize(5)
def gotoBankorBreakfast():
    location = str(input("Do you want to go to bank or breakfast first?"))
    if location == 'bank':
        t.penup()
        t.goto(-200, 200) # Set the turtle position at -200,200
        t.pencolor('green') # Change the color of pen for display on screen
        t.forward(30)
        t.pendown()
        t.fillcolor('orange')
        t.begin_fill()
        #drawing building
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.end_fill()
        t.penup()
        t.forward(-55)
        t.write('I am at Bank and still hungry!', align="right", font=("Verdana", 12, "bold"))
        t.pendown()
        time.sleep(3)
    elif location == 'breakfast':
        t.penup()
        t.goto(-150, 100) # Set the turtle position
        t.pendown()
        t.pencolor('yellow') # Change the color of pen for display on screen
        t.fillcolor('blue')
        t.begin_fill()
        ##turtle.pendown()
        t.pencolor('red')
        ##drawing the triangle
        t.right(35)
        t.forward(125)
        t.right(235)
        t.forward(150)
        t.left(127)
        t.forward(130)
        t.end_fill()
        t.penup()
        t.forward(10)
        t.pendown()
        t.write('I am at Breakfast, yum yum time!', align="right", font=("Verdana", 12, "bold"))
        t.stamp()
        t.forward(2)
        t.penup()
        time.sleep(7)
##        else:
##            t.penup()
##            t.forward(10)
##            t.pencolor('red')
##            t.pendown()
##            t.write('I can only go to bank or breakfast!', align="right", font=("Verdana", 16, "bold"))
##            t.goto(0,0)
def gotoDoctor():
        t.penup()
        t.goto(125,125)
        t.pendown()
        t.write("Whoa, finally I'm at the Doctor!", font=("Verdana", 16, "bold"))
        time.sleep(2)
        
def goBackHome():
        t.penup()
        t.goto(0,0)
        t.pendown
        t.pencolor('blue')
        t.write("Home Sweet Home!", font=("Edwardianscript", 24, "bold"))      
        
def main():
    stepone = gotoBankorBreakfast()
    steptwo = gotoDoctor()
    stepthree = goBackHome()

  

main()


