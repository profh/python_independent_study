# Chapter:		6
# Exercise:		9
# Start:		10:36:19 AM 06/18/2007
# End:			10:38:36 AM 06/18/2007
# Rating:		2
# Note:			Code reuse from chapter 4....
def getGrade(score):
	grades = "FFDCBA"
	return grades[score:score+1]
	
def main():
	print "This program will print out a grade per given score"
	print ""
	
	ingrade = input("What is the student's grade? ")
	print "That student received this grade: %s" % (getGrade(ingrade))

main()