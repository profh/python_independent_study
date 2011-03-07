# Chapter:		5
# Exercise:		3
# Start:		11:36:26 AM 06/11/2007
# End:			11:44:08 AM 06/11/2007
# Rating:		4
# Note:			Good, if you force the student to make a debugging point-getting method

from graphics import *

def main():
	size = 200
	win = GraphWin("Face", size, size)
	
	yellowcircle = Circle(Point(size/2, size/2), (size/2)-10)
	yellowcircle.setOutline("black")
	yellowcircle.setFill("yellow")
	yellowcircle.draw(win)
	
	lefteye = Circle(Point(68, 68), 15)
	lefteye.setOutline("black")
	lefteye.setFill("black")
	lefteye.draw(win)
	
	righteye = Circle(Point(131, 68), 15)
	righteye.setOutline("black")
	righteye.setFill("black")
	righteye.draw(win)
	
	nose = Polygon(Point(99, 97), Point(88, 114), Point(110, 114))
	nose.setFill("black")
	nose.draw(win)
	
	smile = Polygon(Point(39,136), Point(52,150), Point(74,165), Point(105,169), Point(132,162), Point(152,149), Point(162,135))
	smile.setOutline("black")
	smile.setFill("white")
	smile.draw(win)
	
	
	#for debugging/designing
	#while 1:
	#	p = win.getMouse()
	#	print "Point("+str(p.getX())+","+str(p.getY())+"), \r\n"

	win.getMouse() #pause gui window from closing
	win.close()

main()