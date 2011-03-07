# Chapter:		7
# Exercise:		9
# Start:		10:59:44 AM 06/21/2007
# End:			11:02:43 AM 06/21/2007
# Rating:		2
# Note:			basic if/else

def main():
	year = input("Please input a year (1982 - 2048)")
	if (year < 1982 or year > 2048):
		print "Year is out of range"
	else:
		a = year % 19
		b = year % 4
		c = year % 7
		d = (19 * a + 24) % 30
		e = (2 * b + 4 * c + 6 * d + 5) % 7
		easter = 22 + d + e
		month = "March"
		if easter > 31:
			easter-= 31
			month = "April"
		print "The date of easter is",month,easter
main()
