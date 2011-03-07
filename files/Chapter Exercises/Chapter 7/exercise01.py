# Chapter:		7
# Exercise:		1
# Start:		02:32:49 PM 06/20/2007
# End:			02:34:14 PM 06/20/2007
# Rating:		2
# Note:			Shows basic if/else structure

def main():
	hourlypay = input("what is the hourly rate? ")
	hours = input("How many hours worked? ")
	pay = 0.0
	if hours > 40:
		pay = (1.5 * hourlypay) * (hours-40)
		pay += hourlypay * 40
	else:
		pay = hourlypay * hours
	
	print "Pay is $",pay

main()