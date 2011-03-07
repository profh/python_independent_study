# Chapter:	2
# Exercise:	7
# Start:		03:21:48 PM 06/04/2007
# End:		03:24:28 PM 06/04/2007
# Rating:		1
# Note:		Confusing question...

def main():
	print "This program calculates the future value of a X-year investment."
	principal = input("Enter the amount to invest: ")
	years = input("Enter the amount of years for this investment: ")
	apr = input("Enter the annual interest rate: ")
	compoundingperyear = input("Enter the number of times interest is compounded per year: ")
	
	
	for i in range(years*compoundingperyear):
		principal = principal * (1 + (apr/compoundingperyear))

	print "The value in", years, "years is:", principal

main()