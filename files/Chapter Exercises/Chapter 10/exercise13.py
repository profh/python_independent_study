# Chapter:		10
# Exercise:		13
# Start:		02:51:02 AM 07/01/2007
# End:			03:15:06 AM 07/01/2007
# Rating:		4
# Note:			Cool activity...but takes forever.  shows use of class variables

from graphics import *

class Face:
	def __init__(self, window, center, size):
		self.eyeSize = 0.15 * size
		self.eyeOff = size / 3.0
		self.mouthSize = 0.8 * size
		self.mouthOff = size / 2.0
		self.center = center
		self.head = Circle(center, size)
		self.head.draw(window)
		self.window = window
		
		self.leftEye = Line(Point(0,0),Point(0,0))
		self.rightEye = Line(Point(0,0),Point(0,0))
		self.mouth = Line(Point(0,0),Point(0,0))
		

		self.normalEyes()
		self.normalMouth()
		
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
		
	def smile(self):
		self.mouth.undraw()
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
	win = GraphWin("Face", 400, 400)
	f = Face(win, Point(200, 100), 100)
	quit = Button(win, Point(200, 400-40), 80, 40, "Quit")
	
	squintbutton = Button(win, Point(75, 300), 80, 40, "Squint")
	unsquintbutton = Button(win, Point(75+80, 300), 80, 40, "UnSquint")
	smilebutton = Button(win, Point(75+(80*2), 300), 80, 40, "Smile")
	unsmilebutton = Button(win, Point(75+(80*3), 300), 80, 40, "UnSmile")
	
	
	p = win.getMouse()
	while not quit.clicked(p):
		if squintbutton.clicked(p):
			f.squint()
		elif unsquintbutton.clicked(p):
			f.normalEyes()
		elif smilebutton.clicked(p):
			f.smile()
		elif unsmilebutton.clicked(p):
			f.normalMouth()
		
	
		p = win.getMouse()
	
	
main()
