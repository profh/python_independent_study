# Chapter:		5
# Exercise:		2
# Start:		11:07:51 AM 06/11/2007
# End:			11:11:55 AM 06/11/2007
# Rating:		4
# Note:			Shows layering with graphics objects

from graphics import *

def main():

#red, blue, white
	size = 500
	win = GraphWin("Archery Target", size, size)
	
	redcircle = Circle(Point(size/2, size/2), size/2)
	redcircle.setOutline("red")
	redcircle.setFill("red")
	bluecircle = Circle(Point(size/2, size/2), size/2-100)
	bluecircle.setOutline("blue")
	bluecircle.setFill("blue")
	whitecircle = Circle(Point(size/2, size/2), size/2-200)
	whitecircle.setOutline("white")
	whitecircle.setFill("white")
	
	redcircle.draw(win)
	bluecircle.draw(win)
	whitecircle.draw(win)
	
	p = win.getMouse()


	win.close()
main()