# Chapter:		7
# Exercise:		17
# Start:		11:35:57 AM 06/21/2007
# End:			11:41:40 AM 06/21/2007
# Rating:		4
# Note:			Shows how to 'animate'

from time import sleep
from graphics import *

def main():
	width = 400
	height = 100
	circleradius = 20
	win = GraphWin("Animated Bouncing Circle", width, height)
	
	bouncingcircle = Circle(Point(width/2,height/2), circleradius)
	bouncingcircle.setFill("white")
	bouncingcircle.setOutline("black")
	bouncingcircle.draw(win)
	
	curdirection = 1
	
	for i in range(10000):
		newx = bouncingcircle.getCenter().getX() + curdirection
		if (newx+circleradius > width or newx-circleradius < 0):
			curdirection = -1 * curdirection
		bouncingcircle.move(curdirection, 0)
		sleep(0.005)
	win.getMouse()

main()
