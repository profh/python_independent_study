# Chapter:		5
# Exercise:		13
# Start:		12:07:17 PM 06/12/2007
# End:			12:18:58 PM 06/12/2007
# Rating:		2
# Note:			File IO and Looping

from graphics import *

def main():
	input = open("ex13data.txt", "r")
	
	win = GraphWin("Quiz Score Histogram", 500, 200)
	vals = [0,0,0,0,0,0,0,0,0,0,0]
	horizgap = 30
	heightinterval = 10
	
	for line in input:
		num = int(line)
		vals[num] = vals[num]+1
	
	
	for i in range(11):
		t = Text(Point(20+i*(15+horizgap), 180), i)
		t.draw(win)
		p1 = Point(t.getAnchor().getX()-8, 170)
		p2 = Point(p1.getX()+15, p1.getY() - (vals[i]*heightinterval))
		r = Rectangle(p1, p2)
		r.setOutline("black")
		r.setFill("green")
		r.draw(win)
		
		
		
	win.getMouse()

main()
