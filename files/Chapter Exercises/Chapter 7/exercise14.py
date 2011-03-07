# Chapter:		7
# Exercise:		14
# Start:		11:20:09 AM 06/21/2007
# End:			11:22:05 AM 06/21/2007
# Rating:		2
# Note:			first exposure to try/except

import math
from graphics import *

def main():
	radius = input("What is the radius of the circle? ")
	yinter = input("What is the y-intercept of the line? ")
	try:
		width = 200
		height = 200
		win = GraphWin("Circle Intercept", width, height)
		win.setCoords(-10, -10, 10, 10)
		
		Line(Point(0, -10), Point(0, 10)).draw(win)
		Line(Point(-10, 0), Point(10, 0)).draw(win)
		
		c = Circle(Point(0, 0), radius)
		c.setFill("gray")
		c.setOutline("gray")
		c.draw(win)
		
		Line(Point(-10, yinter), Point(10, yinter)).draw(win)
		
		x1 = math.sqrt(radius**2 - yinter**2)
		x2 = -x1
		
		c1 = Circle(Point(x1, yinter), 0.25)
		c1.setFill("red")
		c1.setOutline("black")
		c1.draw(win)
		
		c2 = Circle(Point(x2, yinter), 0.25)
		c2.setFill("red")
		c2.setOutline("red")
		c2.draw(win)
	
		win.getMouse()
	except ValueError:
		print "Error: Line does not intersect circle"

main()
