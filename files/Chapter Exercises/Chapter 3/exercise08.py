# Chapter:	3
# Exercise:	8
# Start:	04:51:37 PM 06/05/2007
# End:		04:56:26 PM 06/05/2007
# Rating:	2
# Note:		Losts of typing in. only one user input.  forces concept that ints are not callable objects

def main():
	print "This program calculates the date of easter based on a given year"
	print ""
	year = input("Please enter in a 4-digit year: ")
	
	C = year / 100
	
	epact = ((8 + (C/4) - C + ((8*C+13)/25) + 11 * ( year % 19)) % 30)
	
	print "The epact for",year,"is",epact

main()