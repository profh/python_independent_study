# Chapter:		7
# Exercise:		16
# Start:		11:24:56 AM 06/21/2007
# End:			11:35:48 AM 06/21/2007
# Rating:		4
# Note:			Caculation of distance and stuff
import math

from graphics import *
def createDot(win, point):
	dot = Circle(point, .5)
	dot.setFill("yellow")
	dot.setOutline("black")
	dot.draw(win)
def getDistance(p1, p2):
	dx = p2.getX() - p1.getX()
	dy = p2.getY() - p1.getY()
	length = math.sqrt(dx**2 + dy**2)
	return length

def main():

#red, blue, white
	size = 500
	win = GraphWin("Archery Target", size, size)
	
	win.setCoords(-10, -10, 10, 10)

	redcircle = Circle(Point(0, 0), 10)
	redcircle.setOutline("red")
	redcircle.setFill("red")
	bluecircle = Circle(Point(0, 0), 8)
	bluecircle.setOutline("blue")
	bluecircle.setFill("blue")
	redcircle1 = Circle(Point(0, 0), 6)
	redcircle1.setOutline("red")
	redcircle1.setFill("red")
	bluecircle1 = Circle(Point(0, 0), 4)
	bluecircle1.setOutline("blue")
	bluecircle1.setFill("blue")
	
	whitecircle = Circle(Point(0, 0), 2)
	whitecircle.setOutline("white")
	whitecircle.setFill("white")
	
	redcircle.draw(win)
	bluecircle.draw(win)
	redcircle1.draw(win)
	bluecircle1.draw(win)
	whitecircle.draw(win)
	totalsum = 0
	for i in range(5):
		p = win.getMouse()
		createDot(win, p)
		dist = getDistance(p, Point(0,0))
		if dist > 10:
			curpointval = 0
		elif dist <= 10 and dist > 8:
			curpointval = 1
		elif dist <= 8 and dist > 6:
			curpointval = 3
		elif dist <= 6 and dist > 4:
			curpointval = 5
		elif dist <= 4 and dist > 2:
			curpointval = 7
		elif dist <= 2:
			curpointval = 9
		
		totalsum += curpointval
		if curpointval != 0:
			print "That shot was worth",curpointval," (total score:"+str(totalsum)+")"
		else:
			print "You Missed!"
	
	print "Your total score is",totalsum
	win.close()
main()
