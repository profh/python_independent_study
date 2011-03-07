# Chapter:		5
# Exercise:		5
# Start:		10:13:44 AM 06/12/2007
# End:			10:26:48 AM 06/12/2007
# Rating:		3
# Note:			Shows use of graphics library. Tedius, yes, but shows what functions are available

from graphics import *

def main():
	width = 520
	height = 125
	spacing = 20
	diewidth = 80
	
	win = GraphWin("Dice", width, height)
	
	die = Rectangle(Point(20, 20), Point(20+diewidth, 20+diewidth))
	die.setOutline("black")
	die.setFill("white")
	
	dot = Circle(Point(20, 20), 5)
	dot.setOutline("black")
	dot.setFill("black")
	
	d1 = die.clone()
	d1.draw(win)
	d2 = die.clone()
	for i in range(5):
		dtemp = die.clone()
		dtemp.move((diewidth + spacing) * i, 0)
		dtemp.draw(win)
	
	dot1 = dot.clone()
	dot1.move(40, 40)
	dot1.draw(win)
	
	dot2 = dot1.clone()
	dot2.move(diewidth+spacing-20, -20)
	dot2.draw(win)
	
	dot3 = dot2.clone()
	dot3.move(40, 40)
	dot3.draw(win)
	
	dot4 = dot3.clone()
	dot4.move(diewidth+spacing, 0)
	dot4.draw(win)
	
	dot5 = dot4.clone()
	dot5.move(-20, -20)
	dot5.draw(win)
	
	dot6 = dot5.clone()
	dot6.move(-20, -20)
	dot6.draw(win)
	
	dot7 = dot2.clone()
	dot7.move(2*(diewidth+spacing), 0)
	dot7.draw(win)
	
	dot8 = dot7.clone()
	dot8.move(0, 40)
	dot8.draw(win)
	
	
	dot9 = dot3.clone()
	dot9.move(2*(diewidth+spacing), 0)
	dot9.draw(win)
	
	dot10 = dot9.clone()
	dot10.move(0, -40)
	dot10.draw(win)
	dot11 = dot10.clone()
	dot11.move(-20, 20)
	dot11.draw(win)
	
	dot12 = dot11.clone()
	dot12.move(diewidth+spacing-20, 0)
	dot12.draw(win)
	dot13 = dot12.clone()
	dot13.move(0, -20)
	dot13.draw(win)
	dot14 = dot12.clone()
	dot14.move(0, 20)
	dot14.draw(win)
	
	dot15 = dot12.clone()
	dot15.move(40, 0)
	dot15.draw(win)
	
	dot16 = dot13.clone()
	dot16.move(40, 0)
	dot16.draw(win)
	dot17 = dot14.clone()
	dot17.move(40, 0)
	dot17.draw(win)
	
	
	
	
	
	win.getMouse()
	win.close()

main()