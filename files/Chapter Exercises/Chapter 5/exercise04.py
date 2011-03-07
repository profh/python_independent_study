# Chapter:		5
# Exercise:		4
# Start:		11:47:19 AM 06/11/2007
# End:			11:56:22 AM 06/11/2007
# Rating:		4
# Note:			Gives user experience with drawing

from graphics import *

def main():
	size = 400
	win = GraphWin("CHristmas Scene", size, size)
	
	sky = Rectangle(Point(0,0), Point(size, size-100))
	sky.setFill("lightblue")
	sky.setOutline("lightblue")
	sky.draw(win)
	
	
	snow = Rectangle(Point(0, size-100), Point(size+2, size+2))
	snow.setFill("white")
	snow.setOutline("black")
	snow.draw(win)
	
	topcircle = Circle(Point(307,204), 16)
	topcircle.setFill("white")
	topcircle.setOutline("black")
	topcircle.draw(win)
	middlecircle = Circle(Point(307,239), 20)
	middlecircle.setFill("white")
	middlecircle.setOutline("black")
	middlecircle.draw(win)
	bottomcircle = Circle(Point(307,278), 25)
	bottomcircle.setFill("white")
	bottomcircle.setOutline("black")
	bottomcircle.draw(win)
	
	
	tree = Rectangle(Point(90,300),  Point(95,198))
	tree.setFill("brown")
	tree.draw(win)
	
	treefoliage = Polygon(Point(92,180),  Point(65,260),  Point(121,260))
	treefoliage.setOutline("green")
	treefoliage.setFill("green")
	treefoliage.draw(win)
	
	
	#for debugging/designing
	while 1:
		p = win.getMouse()
		print "Point("+str(p.getX())+","+str(p.getY())+"), ",

	win.getMouse() #pause gui window from closing
	win.close()

main()