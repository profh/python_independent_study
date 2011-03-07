# Chapter:		6
# Exercise:		16
# Start:		11:03:48 AM 06/18/2007
# End:			11:08:14 AM 06/18/2007
# Rating:		4
# Note:			Shows that you can pass anything to a function (even an object)
from graphics import *

def moveTo(shape, newCenter):
	deltaX = newCenter.getX() - shape.getCenter().getX()
	deltaY = newCenter.getY() - shape.getCenter().getY()
	shape.move(deltaX, deltaY)

def main():
	size = 400
	win = GraphWin("Circle Mover", size, size)
	
	circle = Circle(Point(size/2, size/2), 50)
	circle.setFill("lightblue")
	circle.setOutline("black")
	circle.draw(win)
	
	for i in range(10):
		p = win.getMouse()
		moveTo(circle, p)
	
	win.getMouse()
	

main()
