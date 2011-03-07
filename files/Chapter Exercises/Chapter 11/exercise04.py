# Chapter:		11
# Exercise:		4
# Start:		06:13:43 PM 07/06/2007
# End:			06:34:51 PM 07/06/2007
# Rating:		2
# Note:			Just gui practice

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

	def getStatus(self):
		return self.active
		
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


class Student:

	def __init__(self, name, hours, qpoints):
		self.name = name
		self.hours = float(hours)
		self.qpoints = float(qpoints)
	
	def getName(self):
		return self.name
	
	def getHours(self):
		return self.hours
	
	def getQPoints(self):
		return self.qpoints
	
	def gpa(self):
		return self.qpoints/self.hours
	
	def __str__(self):
		return self.name + ": " + str(self.hours) + ", " + str(self.qpoints)

def makeStudent(infoStr):
    name, hours, qpoints = string.split(infoStr,"\t")
    return Student(name, hours, qpoints)

def cmpName(s1, s2):
	return cmp(s1.getName(), s2.getName())

def cmpHours(s1, s2):
	return cmp(s1.getHours(), s2.getHours())

def cmpQPoints(s1, s2):
	return cmp(s1.getQPoints(), s2.getQPoints())

def main():
	win = GraphWin("GPA Sorter", 400, 300)
	Text(Point(80, 50), "Input File Name: ").draw(win)
	inputname = Entry(Point(250, 50), 20)
	inputname.draw(win)
	Text(Point(80, 100), "Output File Name: ").draw(win)
	outputname = Entry(Point(250, 100), 20)
	outputname.draw(win)
	
	Text(Point(80, 150), "Sorting Order: ").draw(win)
	ascbutton = Button(win, Point(200, 150), 100, 20, "Ascending")
	ascbutton.activate()
	descbutton = Button(win, Point(320, 150),100, 20, "Descending")
	descbutton.activate()
	
	Text(Point(80, 200), "Sorting Key: ").draw(win)
	namebutton = Button(win, Point(170, 200), 75, 20, "Name")
	namebutton.activate()
	
	hoursbutton = Button(win, Point(250, 200), 75, 20, "Hours")
	hoursbutton.activate()
	
	qpointsbutton = Button(win, Point(330, 200), 75, 20, "QPoints")
	qpointsbutton.activate()
	
	quitbutton = Button(win, Point(50, 20), 75, 20, "Quit")
	quitbutton.activate()
	
	processbutton = Button(win, Point(200, 250), 200, 40, "Process")
	processbutton.activate()
	
	m = win.getMouse()
	ascdesc = ""
	sortby = ""
	while not quitbutton.clicked(m):
		if ascbutton.clicked(m):
			ascdesc = "asc"
		elif descbutton.clicked(m):
			ascdesc = "desc"
		elif namebutton.clicked(m):
			sortby = "name"
		elif hoursbutton.clicked(m):
			sortby = "hours"
		elif qpointsbutton.clicked(m):
			sortby = "qpoints"
		elif processbutton.clicked(m):
			run(inputname.getText(), outputname.getText(), sortby, ascdesc)
			break
		m = win.getMouse()
		
	win.close()
		


def run(infilename, outfilename, sortby, ascdesc):
	print infilename
	print outfilename
	print sortby
	print ascdesc
	
	infile = open(infilename, 'r')
	students = []
	for line in infile:
		students.append(makeStudent(line))
	
	infile.close()
	
	if ascdesc == "asc":
		reverse = False
	elif ascdesc == "desc":
		reverse = True

	if sortby == "name":
		students.sort(cmpName, reverse=reverse)
	elif sortby == "hours":
		students.sort(cmpHours, reverse=reverse)
	elif sortby == "qpoints":
		students.sort(cmpQPoints, reverse=reverse)
	
	outfile = open(outfilename, "w")
	for s in students:
		outfile.write(s+"\r\n")
	outfile.close()

	
main()
