# Chapter:		10
# Exercise:		14
# Start:		03:15:52 AM 07/01/2007
# End:			03:28:49 AM 07/01/2007
# Rating:		4
# Note:			Fun exercise that demonstrates how you can make graphic objects (widgets) and easily manage them

from graphics import *
from random import randrange
from time import sleep

class Face:
	def __init__(self, window, center, size):
		self.size = size
		self.eyeSize = 0.15 * size
		self.eyeOff = size / 3.0
		self.mouthSize = 0.8 * size
		self.mouthOff = size / 2.0
		self.center = center
		self.window = window
		
		self.head = Line(Point(0,0), Point(0,0))
		self.leftEye = Line(Point(0,0),Point(0,0))
		self.rightEye = Line(Point(0,0),Point(0,0))
		self.mouth = Line(Point(0,0),Point(0,0))
		
		self.smileToggle = False
		self.squintToggle= False
		
		self.normalHead()
		self.normalEyes()
		self.normalMouth()
	
	def move(self, deltaX, deltaY):
		newpt = Point(self.center.getX()+deltaX, self.center.getY()+deltaY)
		self.center = newpt
		self.normalHead()
		
		if self.squintToggle:
			self.squint()
		else:
			self.normalEyes()
			
		if self.smileToggle:
			self.smile()
		else:
			self.normalMouth()
		
	def getCenter(self):
		return self.center
	
	def normalHead(self):
		self.head.undraw()
		self.head = Circle(self.center, self.size)
		self.head.draw(self.window)

		
	def normalEyes(self):
		self.leftEye.undraw()
		self.rightEye.undraw()
		
		self.leftEye = Circle(self.center, self.eyeSize)
		self.leftEye.move(-self.eyeOff, -self.eyeOff)
		self.rightEye = Circle(self.center, self.eyeSize)
		self.rightEye.move(self.eyeOff, -self.eyeOff)
		self.leftEye.draw(self.window)
		self.rightEye.draw(self.window)
		
	def normalMouth(self):
		self.mouth.undraw()
		
		self.p1 = self.center.clone()
		self.p1.move(-self.mouthSize/2, self.mouthOff)
		self.p2 = self.center.clone()
		self.p2.move(self.mouthSize/2, self.mouthOff)
		self.mouth = Line(self.p1, self.p2)
		self.mouth.draw(self.window)
		
	def switcheyes(self):
		if self.squintToggle:
			self.squintToggle = False
			self.normalEyes()
		else:
			self.squintToggle = True
			self.squint()

	
	def switchmouth(self):
		if self.smileToggle:
			self.smileToggle = False
			self.normalMouth()
		else:
			self.smileToggle = True
			self.smile()
	
	def smile(self):
		self.mouth.undraw()
		self.p1 = self.center.clone()
		self.p1.move(-self.mouthSize/2, self.mouthOff)
		self.p2 = self.center.clone()
		self.p2.move(self.mouthSize/2, self.mouthOff)
		self.p3 = self.center.clone()
		self.p3.move(0, self.mouthOff+40)
		self.mouth = Polygon(self.p1, self.p2, self.p3)
		self.mouth.draw(self.window)
		
	def squint(self):		
		self.leftEye.undraw()
		self.rightEye.undraw()
		p1 = self.center.clone()
		p1.move(-self.eyeOff, -self.eyeOff)
		pa = Point(p1.getX()-(self.eyeSize/2), p1.getY());
		pb = Point(p1.getX()+(self.eyeSize/2), p1.getY());
		
		self.leftEye = Line(pa, pb)
		self.leftEye.draw(self.window)
		
		p1 = self.center.clone()
		p1.move(self.eyeOff, -self.eyeOff)
		pa = Point(p1.getX()-(self.eyeSize/2), p1.getY());
		pb = Point(p1.getX()+(self.eyeSize/2), p1.getY());
		
		self.rightEye = Line(pa, pb)
		self.rightEye.draw(self.window)
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
        self.activate()

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
	width = 400
	height = 200
	win = GraphWin("Face", width, height)
	circleradius = 100
	curdirection = 1
	f = Face(win, Point(width/2, 100), circleradius)
	for i in range(10000):
		newx = f.getCenter().getX() + curdirection
		if (newx+circleradius > width or newx-circleradius < 0):
			curdirection = -1 * curdirection
			if randrange(0, 2) == 0:
				f.switchmouth()
			else:
				f.switcheyes()
			
		f.move(curdirection, 0)
		sleep(0.005)
	
	
main()
