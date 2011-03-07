# Chapter:		10
# Exercise:		5
# Start:		01:55:55 AM 07/01/2007
# End:			02:01:15 AM 07/01/2007
# Rating:		2
# Note:			justs adds a mutator

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
	
	def addGrade(self, gradePoint, credits):
		self.hours += credits
		self.qpoints += gradePoint
		

def main():
	s = Student("Ari Rubinstein", 0, 0)
	s.addGrade(4.0, 9.0)
	s.addGrade(3.8, 9.0)
	s.addGrade(2.6, 12.0)
	print "Hours:",s.getHours()
	print "QualityPoints:",s.getQPoints()
	print "GPA for",s.getName(),"is",s.gpa()*10

main()
