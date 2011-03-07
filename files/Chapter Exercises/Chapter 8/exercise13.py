# Chapter:		8
# Exercise:		13
# Start:		11:19:59 AM 06/25/2007
# End:			11:37:05 AM 06/25/2007
# Rating:		4
# Note:			Tedious math

from graphics import *
def drawCircle(win, point):
	c = Circle(point, 3)
	c.setOutline("black")
	c.setFill("black")
	c.draw(win)

def regressionline(win, vals):
	xtot = 0
	ytot = 0
	n = len(vals)
	for point in vals:
		xtot += point.getX()
		ytot += point.getY()
	xmean = float(xtot)/float(len(vals))
	ymean = float(ytot)/float(len(vals))

	sTop = 0.0
	sBottom = 0.0
	
	for point in vals:
		sTop += (point.getX() * point.getY() - n * xmean * ymean)
		sBottom += (point.getX()**2 - n*xmean**2)
		
	
	m = sTop/sBottom

	l = Line(Point(0,ymean), Point(400, m*ymean)).draw(win)


def main():
	height = 400
	width = 400
	win = GraphWin("Regression Line Plotter", width, height)
	donebutton = Rectangle(Point(1, height-20), Point(80, height))
	donebutton.setOutline("black")
	donebutton.setFill("yellow")
	donebutton.draw(win)
	Text(Point(40, height-10), "Done").draw(win)
	points = []
	while True:
		m = win.getMouse()
		if m.getX() < 80 and m.getY() > height-20:
			break
		drawCircle(win, m)
		points.append(m)
		
	regressionline(win, points)	
	
	win.getMouse()
	win.close()
	
	
	

main()



