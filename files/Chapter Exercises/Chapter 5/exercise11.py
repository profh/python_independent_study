# Chapter:		5
# Exercise:		11
# Start:		11:27:04 AM 06/12/2007
# End:			11:49:13 AM 06/12/2007
# Rating:		2
# Note:			Tedious math and annoying plot-cordination

import math
from graphics import *

def main():
	
	width = 400
	height = 400
	tempcircleradius = 5
	
	
	win = GraphWin("5-click house", width, height)
	
	print "First Click: Corner of the rectangular frame of the house"
	p1 = win.getMouse()
	c1 = Circle(p1, tempcircleradius)
	c1.setFill("black")
	c1.setOutline("black")
	c1.draw(win)
	
	print "Second Click: Corner of the rectangular frame of the house"
	p2 = win.getMouse()
	c2 = Circle(p2, tempcircleradius)
	c2.setFill("black")
	c2.setOutline("black")
	c2.draw(win)

	if p1.getY() > p2.getY():
		housebottom = p1
		housetop = p2
	else:
		housebottom = p2
		housetop = p1
	

	
	r = Rectangle(p1, p2)
	r.setFill("#FFA95F")
	r.setOutline("black")
	r.draw(win)
	
	#get rid of guides
	c1.undraw()
	c2.undraw()
	
	print "Third Click: Center top edge of door"
	p3 = win.getMouse()
	
	doorwidth = (1.0/5.0) * abs(p2.getX()-p1.getX())
	doortopleft = Point(p3.getX()-(doorwidth/2), p3.getY())
	
	doorbottomright = Point(doortopleft.getX()+doorwidth, housebottom.getY())
	
	door = Rectangle(doortopleft, doorbottomright)
	door.setOutline("black")
	door.setFill("#AD4E00")
	door.draw(win)
	
	print "Fourth Click: Center of square window"
	p4 = win.getMouse()
	windowwidth = doorwidth/2.0
	
	wintopleft = Point(p4.getX() - (windowwidth/2), p4.getY() - (windowwidth/2))
	winbottomright = Point(wintopleft.getX()+windowwidth, wintopleft.getY()+windowwidth)
	window = Rectangle(wintopleft, winbottomright)
	window.setOutline("black")
	window.setFill("#85C4FF")
	window.draw(win)
	
	print "Fifth Click: Top of roof"
	p5 = win.getMouse()
	housewidth = abs(p2.getX()-p1.getX())
	
	if housetop.getX() < housebottom.getX():
		top = housetop.getX()
	else:
		top = housebottom.getX()
	
	housetopleft = Point(top, housetop.getY())
	housetopright = Point(housetopleft.getX() + housewidth, housetopleft.getY())
	
	roof = Polygon(p5, housetopleft, housetopright)
	roof.setOutline("black")
	roof.setFill("#FFA95F")
	roof.draw(win)
	
	
	
	
	
	
	
	
	raw_input("Press Enter to continue")
	win.close()
main()