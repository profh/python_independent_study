# Chapter:		5
# Exercise:		1
# Start:		11:01:16 AM 06/11/2007
# End:			11:07:00 AM 06/11/2007
# Rating:		4
# Note:			Shows use of graphics library

from graphics import *

def main():
	width = 20
	win = GraphWin()
	shape = Rectangle(Point(50, 50), Point(50+width, 50+width))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()
		newshape = Rectangle(Point(p.getX()-(width/2), p.getY()-(width/2)), Point(p.getX()+(width/2), p.getY()+(width/2)))
		newshape.setOutline("red")
		newshape.setFill("red")
		newshape.draw(win)
		if i == 8:
			textobj = Text(Point(80,20), "Click again to quit")
			textobj.draw(win)

	win.close()
main()