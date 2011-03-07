# Chapter:		9
# Exercise:		14
# Start:		01:16:06 AM 07/01/2007
# End:			01:23:38 AM 07/01/2007
# Rating:		4
# Note:			neat little program. involves graphics and random lib

from graphics import *
from random import randrange, random
from time import sleep
import math

def main():
	n = input("Number of steps? ")
	size = 400
	win = GraphWin("Random Walk", size, size)
	curpos = Point(size/2, size/2)
	walkdistance = 10
	for i in range(n):
		angle = random() * 2 * math.pi
		x = curpos.getX() + walkdistance * math.cos(angle)
		y = curpos.getY() + walkdistance * math.sin(angle)
		newpos = Point(x, y)
		Line(curpos, newpos).draw(win)
		curpos = newpos
		sleep(0.005)
	win.getMouse()
	


main()
