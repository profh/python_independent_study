# Chapter:		5
# Exercise:		6
# Start:		10:31:26 AM 06/12/2007
# End:			10:41:42 AM 06/12/2007
# Rating:		3
# Note:			Shows use of Entry objects

from graphics import *

def main():

	inputwin = GraphWin("Future Value Plotter", 300, 120)
	
	Text(Point(130, 30), "Initial Principal: ").draw(inputwin)
	Text(Point(100, 60), "Annualized interest Rate: ").draw(inputwin)
	
	principalin = Entry(Point(220, 30), 5)
	principalin.draw(inputwin)
	
	aprin = Entry(Point(220, 60), 5)
	aprin.draw(inputwin)
	
	button = Rectangle(Point(150, 80), Point(290, 100))
	button.setOutline("black")
	button.setFill("white")
	button.draw(inputwin)
	Text(Point(220, 90), "Click to Continue").draw(inputwin)
	
	
	inputwin.getMouse()
	inputwin.close()
	
	
	
	# Get principal and interest rate
	principal = eval(principalin.getText())
	apr = eval(aprin.getText())

	# Create a graphics window with labels on left edge
	win = GraphWin("Investment Growth Chart", 320, 240)
	win.setBackground("white")
	Text(Point(20, 230), ' 0.0K').draw(win)
	Text(Point(20, 180), ' 2.5K').draw(win)
	Text(Point(20, 130), ' 5.0K').draw(win)
	Text(Point(20, 80), ' 7.5k').draw(win)
	Text(Point(20, 30), '10.0K').draw(win)

	# Draw bar of initial principal
	height = principal * 0.02
	bar = Rectangle(Point(40, 230), Point(65, 230-height))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	# Draw bars for successive years
	for year in range(1,11):
		# calculate value for the next year
		principal = principal * (1 + apr)
		# draw bar for this value
		xll = year * 25 + 40
		height = principal * 0.02
		bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	raw_input("Press <Enter> to quit.")
	win.close()

main()


