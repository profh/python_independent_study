# Chapter:		7
# Exercise:		11
# Start:		11:07:02 AM 06/21/2007
# End:			11:08:29 AM 06/21/2007
# Rating:		2
# Note:			basic if/else

def main():
	year = input("What is the year? ")
	if year % 400 == 0:
		print year,"is a leap year"
	else:
		print year,"is not a leap year"
main()
