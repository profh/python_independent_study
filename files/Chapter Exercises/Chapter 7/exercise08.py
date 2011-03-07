# Chapter:		7
# Exercise:		8
# Start:		10:54:44 AM 06/21/2007
# End:			10:57:52 AM 06/21/2007
# Rating:		3
# Note:			Cool if loops

def main():
	age = input("What is the person's age? ")
	yearsofcitizenship = input("How many years of citizenship? ")
	
	if age < 30:
		print "You are too young to be a US senator"
	elif yearsofcitizenship < 9:
		print "You have not lived in the US for enough time to become a US senator"
	else:
		print "You can be a US senator"
	
	if age < 25:
		print "You are too young to be a US representative"
	elif yearsofcitizenship < 7:
		print "You have not lived in the US for enough time to become a US representative"
	else:
		print "You can be a US representative"
	
main()
