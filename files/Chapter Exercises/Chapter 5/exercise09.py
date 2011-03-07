# Chapter:		5
# Exercise:		9
# Start:		10:57:44 AM 06/12/2007
# End:			11:01:16 AM 06/12/2007
# Rating:		3
# Note:			User constructed rectangle.  Some math functions. use of abs

import math
from graphics import *

def main():
	
	width = 200
	height = 200
	win = GraphWin("Rectangle Info", width, height)
	win.setCoords(-10, -10, 10, 10)
	
	Line(Point(0, -10), Point(0, 10)).draw(win)
	Line(Point(-10, 0), Point(10, 0)).draw(win)
	
	p1 = win.getMouse()
	c1 = Circle(p1, 0.4)
	c1.setFill("black")
	c1.setOutline("black")
	c1.draw(win)
	
	p2 = win.getMouse()
	c2 = Circle(p2, 0.4)
	c2.setFill("black")
	c2.setOutline("black")
	c2.draw(win)
	
	r = Rectangle(p1, p2)
	r.setFill("gray")
	r.setOutline("black")
	r.draw(win)

	length = abs(p1.getY()-p2.getY())
	width = abs(p1.getX()-p2.getX())
	area = length*width
	perimeter = 2*(length + width)
	
	print "Area =",area
	print "Perimeter =",perimeter
	
	
	raw_input("Press Enter to continue")
	win.close()
main()