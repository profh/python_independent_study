# Chapter:		10
# Exercise:		4
# Start:		01:50:04 AM 07/01/2007
# End:			01:55:22 AM 07/01/2007
# Rating:		4
# Note:			Neat activity.  An actually useful, but boring, app

from random import randrange
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
	p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0

def main():
	win = GraphWin("Three Button Monte.", 350, 200)
	b1 = Button(win, Point(75, 50), 75, 40, "Button 1")
	b1.activate()
	b2 = Button(win, Point(175, 50), 75, 40, "Button 2")
	b2.activate()
	b3 = Button(win, Point(275, 50), 75, 40, "Button 3")
	b3.activate()
	quitbutton = Button(win, Point(175, 150), 50, 40, "Quit")
	quitbutton.activate()
	p = win.getMouse()
	while not quitbutton.clicked(p):
		magicbutton = randrange(1, 4)
		if (b1.clicked(p) and magicbutton == 1) or (b2.clicked(p) and magicbutton == 2) or (b3.clicked(p) and magicbutton == 31):
			t = Text(Point(175, 100), "You Win. Magic Button was "+str(magicbutton))
			t.draw(win)
		elif (b1.clicked(p) and magicbutton != 1) or (b2.clicked(p) and magicbutton != 2) or (b3.clicked(p) and magicbutton != 31):
			t = Text(Point(175, 100), "You Lose. Magic Button was "+str(magicbutton))
			t.draw(win)
		else:
			t = Text(Point(175, 100), "Please Click on a button")
			t.draw(win)
			
		p = win.getMouse()
		t.undraw()
		b1.activate()
		b2.activate()
		b3.activate()
		

main()