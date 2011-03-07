# Chapter:		7
# Exercise:		15
# Start:		11:22:37 AM 06/21/2007
# End:			11:24:29 AM 06/21/2007
# Rating:		4
# Note:			Shows how you can use try-catches to change output, rather than just erring out

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
	try:
		slope = dy/dx
	except ZeroDivisionError:
		slope = "Undefined"

	length = math.sqrt(dx**2 + dy**2)
	
	
	print "dx =",dx
	print "dy =",dy
	print "slope =",slope
	print "length =",length
	raw_input("Press Enter to continue")
	win.close()
main()
