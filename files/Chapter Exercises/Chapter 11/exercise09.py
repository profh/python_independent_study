# Chapter:		11
# Exercise:		9
# Start:		07:01:47 PM 07/06/2007
# End:			07:04:52 PM 07/06/2007
# Rating:		3
# Note:			Speedier sorting

# gpa.py
#    Program to find student with highest GPA
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

def makeStudent(infoStr):
    name, hours, qpoints = string.split(infoStr,"\t")
    return (qpoints, Student(name, hours, qpoints))

def main():
	filename = raw_input("Enter name the grade file: ")
	infile = open(filename, 'r')
	best = makeStudent(infile.readline())
	students = []
	for line in infile:
		students.append(makeStudent(line))
	infile.close()
	
	students.sort()
	print students
	
if __name__ == '__main__':
    main()

