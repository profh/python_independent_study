# Chapter:		6
# Exercise:		6
# Start:		10:23:11 AM 06/18/2007
# End:			10:26:51 AM 06/18/2007
# Rating:		2
# Note:			Code Reuse
import math
from graphics import *
def getarea(a, b, c):
	s = (a+b+c)/2
	A = math.sqrt(s * (s - a)*(s - b)*(s - c))
	return A

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText("The perimeter is: %0.2f" % perim)
    win.getMouse()
    message.setText("Area is: %0.2f" % getarea(distance(p1,p2), distance(p2,p3), distance(p3,p1)))

    # Wait for another click to exit
    win.getMouse()

main()
