# Chapter:		7
# Exercise:		4
# Start:		10:36:14 AM 06/21/2007
# End:			10:38:51 AM 06/21/2007
# Rating:		3
# Note:			Shows how you can use elseifs based on criteria

def main():
	units = input("What is the number of units for the student? ")
	if units >= 26:
		status = "Senior"
	elif units >= 16:
		status = "Junior"
	elif units >= 7:
		status = "Sophomore"
	else:
		status = "Freshman"
	
	print "Student with %d units is a %s"%(units, status)

main()
