from graphics import *
import random
import time

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
#for line in datafile: print(line)


# Do some simple drawing
window = GraphWin("Visualisation", 300, 300)

x = 0

for line in datafile:
    print(line)

    x += 6
    num = int(float(line))
    box = Rectangle(Point(x,num),Point(x+6,num))
    box.setFill(color_rgb(num,num,num))
    box.draw(window)
    
    box = Rectangle(Point(num,x),Point(x+6,num))
    box.setFill(color_rgb(num,num,num))
    box.draw(window)

    box = Rectangle(Point(x,x),Point(x+6,num))
    box.setFill(color_rgb(num,num,num))
    box.draw(window)

    box = Rectangle(Point(x+6,num),Point(num,x))
    box.setFill(color_rgb(num,num,num))
    box.draw(window)

    box = Rectangle(Point(x+6,num),Point(x,x))
    box.setFill(color_rgb(num,num,num))
    box.draw(window)
    
 
   
# Waits until the mouse is clicked before closing the window
window.getMouse()
