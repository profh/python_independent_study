# Chapter:		7
# Exercise:		2
# Start:		10:30:47 AM 06/21/2007
# End:			10:33:33 AM 06/21/2007
# Rating:		2
# Note:			Basic if/else

def main():
	grade = input("What is the student's grade? ")
	if grade == 0 or grade == 1:
		letter = "F"
	elif grade == 2:
		letter = "D"
	elif grade == 3:
		letter = "C"
	elif grade == 4:
		letter = "B"
	elif grade == 5:
		letter = "A"
	
	print "The student's letter grade is %s"%letter
		


main()
