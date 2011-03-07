# Chapter:		6
# Exercise:		15
# Start:		10:49:08 AM 06/18/2007
# End:			10:56:26 AM 06/18/2007
# Rating:		4
# Note:			Code Reuse...But shows how you can use functions with graphics

from graphics import *
def drawFace(center, size, win):
	yellowcircle = Circle(center, size)
	yellowcircle.setOutline("black")
	yellowcircle.setFill("yellow")
	yellowcircle.draw(win)
	
	lefteye = Circle(Point(center.getX()-42, center.getY()-42), 15)
	lefteye.setOutline("black")
	lefteye.setFill("black")
	lefteye.draw(win)
	
	righteye = Circle(Point(center.getX()+42, center.getY()-42), 15)
	righteye.setOutline("black")
	righteye.setFill("black")
	righteye.draw(win)
	
	nose = Polygon(Point(center.getX()-1, center.getY()-2), Point(center.getX()-12, center.getY()+14), Point(center.getX()+10, center.getY()+14))
	nose.setFill("black")
	nose.draw(win)
	
	smile = Polygon(Point(center.getX()-61,center.getY()+36), Point(center.getX()-42,center.getY()+50), Point(center.getX()-26,center.getY()+65), Point(center.getX()+5,center.getY()+69), Point(center.getX()+32,center.getY()+62), Point(center.getX()+52,center.getY()+49), Point(center.getX()+62,center.getY()+35))
	smile.setOutline("black")
	smile.setFill("white")
	smile.draw(win)



def main():
	size = 200
	win = GraphWin("Face", size, size)
	drawFace(Point(100,100), 60, win)
	drawFace(Point(200,100), 60, win)
	win.getMouse()
	

main()
