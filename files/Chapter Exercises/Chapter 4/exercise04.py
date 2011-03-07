# Chapter:	4
# Exercise:	4
# Start:	07:12:37 PM 06/10/2007
# End:		07:15:27 PM 06/10/2007
# Rating:	3
# Note:		shows control structures

def main():
	grade = input("What is the number grade? ")
	if grade >= 90 and grade <= 100:
		print "A"
	elif grade >= 80 and grade < 90:
		print "B"
	elif grade >= 70 and grade < 80:
		print "C"
	elif grade >= 60 and grade < 70:
		print "D"
	elif grade < 60:
		print "E"

main()