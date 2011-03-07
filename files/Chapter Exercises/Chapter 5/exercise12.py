# Chapter:		5
# Exercise:		12
# Start:		11:55:37 AM 06/12/2007
# End:			12:06:05 PM 06/12/2007
# Rating:		3
# Note:			Uses file input for drawing

from graphics import *

def main():
	input = open("ex12data.txt", "r")
	count = int(input.readline())
	win = GraphWin("Student Exam Scores", 400, count*40)
	verticalentrysize = 30
	
	
	for i in range(count):
		data = input.readline()
		data = data.split()
		name = data[0]
		grade = int(data[1])
		Text(Point(100, 20+i*verticalentrysize + (verticalentrysize/2)), name).draw(win)
		
		p1 = Point(150, 20+i*verticalentrysize)
		p2 = Point(150 + grade, 20+i*verticalentrysize+verticalentrysize)
		
		bar = Rectangle(p1, p2)
		
		bar.setOutline("black")
		bar.setFill("green")
		bar.draw(win)

	win.getMouse()

main()
