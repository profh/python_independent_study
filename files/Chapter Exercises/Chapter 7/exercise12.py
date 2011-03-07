# Chapter:		7
# Exercise:		12
# Start:		11:09:37 AM 06/21/2007
# End:			11:13:14 AM 06/21/2007
# Rating:		3
# Note:			Uses string.split
def isLeapYear(year):
	if year % 400 == 0:
		return 1
	else:
		return 0
	
def main():
	date = raw_input("Please enter in date in form of month/day/year: ")
	date = date.split("/")
	month = int(date[0])
	day = int(date[1])
	year = int(date[2])
	
	maxdays = [31,28+isLeapYear(year),31,30,31,30,31,31,29,31,30,29]
	
	if month < 1 or month > 12:
		print "Month is invalid"
	elif day < 0 or day > 31:
		print "Day is invalid"
	elif year < 0:
		print "Year is invalid"
	elif day > maxdays[month-1]:
		print "That day does not exist in that month"	
	else:
		print "That date is valid"
	
	
main()
