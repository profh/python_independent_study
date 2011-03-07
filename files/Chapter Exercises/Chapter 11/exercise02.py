# Chapter:		11
# Exercise:		2
# Start:		05:59:39 PM 07/06/2007
# End:			06:09:41 PM 07/06/2007
# Rating:		3
# Note:			Shows use of custom compare functions

import string

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
	filename = raw_input("Enter name the grade file: ")
	infile = open(filename, 'r')
	students = []
	for line in infile:
		students.append(makeStudent(line))
	
	infile.close()
	
	sortby = raw_input("Sort By (name, hours, qpoints): ")
	if sortby == "name":
		students.sort(cmpName)
	elif sortby == "hours":
		students.sort(cmpHours)
	elif sortby == "qpoints":
		students.sort(cmpQPoints)
	else:
		print "Input unknown.  Not Sorting"
	
	for s in students:
		print s


if __name__ == '__main__':
	main()
	
