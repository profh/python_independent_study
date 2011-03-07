# Chapter:		7
# Exercise:		3
# Start:		10:34:01 AM 06/21/2007
# End:			10:35:53 AM 06/21/2007
# Rating:		2
# Note:			Basic if/else statements

def main():
	grade = input("What is the student's grade? ")
	if grade >= 90:
		letter = "A"
	elif grade >= 80 and grade < 90:
		letter = "B"
	elif grade >= 70 and grade < 80:
		letter = "C"
	elif grade >= 60 and grade < 70:
		letter = "D"
	elif grade >= 50 and grade < 60:
		letter = "E"
	elif grade < 60:
		letter = "F"
	
	print "The student's letter grade is: %s"%letter

main()
