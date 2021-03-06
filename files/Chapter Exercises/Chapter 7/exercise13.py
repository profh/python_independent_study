# Chapter:		7
# Exercise:		13
# Start:		11:14:40 AM 06/21/2007
# End:			11:19:57 AM 06/21/2007
# Rating:		3
# Note:			Uses some functions
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
		dayNum = 31 * (month - 1) + day
		if month > 2:
			dayNum -= (4*month + 23) / 10
		if isLeapYear(year) == 1 and month > 2:
			dayNum += 1
		print "Day number",dayNum
	
main()
