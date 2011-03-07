# Chapter:		5
# Exercise:		10
# Start:		11:16:06 AM 06/12/2007
# End:			11:21:35 AM 06/12/2007
# Rating:		3
# Note:			Deals with math functions.  Shows use of coordinate plotting system

import math
from graphics import *

def main():
	
	width = 200
	height = 200
	win = GraphWin("Triangle Info", width, height)
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
	
	p3 = win.getMouse()
	c3 = Circle(p3, 0.4)
	c3.setFill("black")
	c3.setOutline("black")
	c3.draw(win)
	
	p = Polygon(p1, p2, p3)
	p.setFill("gray")
	p.setOutline("black")
	p.draw(win)
	
	a = math.sqrt((p2.getX()-p1.getX())**2 + (p2.getY()-p1.getY())**2)
	b = math.sqrt((p3.getX()-p2.getX())**2 + (p3.getY()-p2.getY())**2)
	c = math.sqrt((p1.getX()-p3.getX())**2 + (p1.getY()-p3.getY())**2)
	
	s = (a + b + c) / 2
	
	area = math.sqrt(s * (s-a) * (s-b) * (s-c))
	
	perimeter = a + b + c
	
	print "Length of A:",a
	print "Length of B:",b
	print "Length of C:",c
	print "Perimeter:",perimeter
	print "S:",s
	print "Area:",area
	
	
	
	raw_input("Press Enter to continue")
	win.close()
main()