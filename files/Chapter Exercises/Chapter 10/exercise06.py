# Chapter:		10
# Exercise:		6
# Start:		02:01:38 AM 07/01/2007
# End:			02:07:54 AM 07/01/2007
# Rating:		2
# Note:			Adding another method.  nothing new

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
	
	def addLetterGrade(self, lettergrade, credits):
		lettergrade = lettergrade.upper()
		if lettergrade == "A+" or lettergrade == "A":
			self.addGrade(4.0, credits)
		elif lettergrade == "A-":
			self.addGrade(3.7, credits)
		elif lettergrade == "B+":
			self.addGrade(3.3, credits)
		elif lettergrade == "B":
			self.addGrade(3.0, credits)
		elif lettergrade == "B-":
			self.addGrade(2.7, credits)
		elif lettergrade == "C+":
			self.addGrade(2.3, credits)
		elif lettergrade == "C":
			self.addGrade(2.0, credits)
		elif lettergrade == "C-":
			self.addGrade(1.7, credits)
		elif lettergrade == "D+":
			self.addGrade(1.3, credits)
		elif lettergrade == "D":
			self.addGrade(1.0, credits)
		elif lettergrade == "D-":
			self.addGrade(0.7, credits)
		elif lettergrade == "E+":
			self.addGrade(0.3, credits)
		elif lettergrade == "E":
			self.addGrade(0.0, credits)
		elif lettergrade == "F":
			self.addGrade(0.0, credits)
		else:
			print "Error interpreting letter grade"
		
			
		

def main():
	s = Student("Ari Rubinstein", 0, 0)
	s.addGrade(4.0, 9.0)
	s.addGrade(3.8, 9.0)
	s.addGrade(2.6, 12.0)
	s.addLetterGrade("A", 9)
	s.addLetterGrade("A+", 9)
	s.addLetterGrade("B-", 9)
	s.addLetterGrade("B-", 9)
	print "Hours:",s.getHours()
	print "QualityPoints:",s.getQPoints()
	print "GPA for",s.getName(),"is",s.gpa()*10

main()
