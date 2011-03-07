# Chapter:		7
# Exercise:		10
# Start:		11:04:39 AM 06/21/2007
# End:			11:06:00 AM 06/21/2007
# Rating:		3
# Note:			Shows use of specific data instead of ranges
def main():
	year = input("Please input a year (1900 - 2099)")
	if (year < 1900 or year > 2099):
		print "Year is out of range"
	else:
		a = year % 19
		b = year % 4
		c = year % 7
		d = (19 * a + 24) % 30
		e = (2 * b + 4 * c + 6 * d + 5) % 7
		easter = 22 + d + e
		
		if year == 1954 or year == 1981 or year == 2049 or year == 2076:
			easter -= 7
		
		month = "March"
		if easter > 31:
			easter-= 31
			month = "April"
		print "The date of easter is",month,easter

main()
