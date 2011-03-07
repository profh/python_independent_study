# Chapter:	4
# Exercise:	3
# Start:	10:46:13 AM 06/06/2007
# End:		10:48:27 AM 06/06/2007
# Rating:	3
# Note:		Shows use of array slicing.  This can be done via array slicing or a list and using the index as the value....or a dictionary....or an if statement...you get the drift

def main():
	print "This program will print out a grade per given score"
	print ""
	
	grades = "FFDCBA"
	ingrade = input("What is the student's grade? ")
	print "That student received this grade: %s" % (grades[ingrade:ingrade+1])
	
main()
