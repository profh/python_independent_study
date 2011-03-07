# Chapter:		5
# Exercise:		8
# Start:		10:52:40 AM 06/12/2007
# End:			10:57:02 AM 06/12/2007
# Rating:		4
# Note:			Shows current user input and calculations based on user input

import math
from graphics import *

def main():
	
	width = 200
	height = 200
	win = GraphWin("Line Segment Info", width, height)
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
	
	Line(p1, p2).draw(win)
	
	dx = p2.getX() - p1.getX()
	dy = p2.getY() - p1.getY()
	slope = dy/dx
	length = math.sqrt(dx**2 + dy**2)
	
	
	print "dx =",dx
	print "dy =",dy
	print "slope =",slope
	print "length =",length
	raw_input("Press Enter to continue")
	win.close()
main()