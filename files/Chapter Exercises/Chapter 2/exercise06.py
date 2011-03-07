# Chapter:	2
# Exercise:	6
# Start:		03:19:39 PM 06/04/2007
# End:		03:20:32 PM 06/04/2007
# Rating:		3
# Note:		makes the student change variables and modify the formula

def main():
	print "This program calculates the future value of a X-year investment."
	years = input("Enter the amount of years for this investment: ")
	
	amounteachyear = input("Enter the amount to invest per year: ")
	apr = input("Enter the annual interest rate: ")
	principal = 0
	
	for i in range(years):
		principal = (principal + amounteachyear) * (1 + apr)

	print "The value in", years, "years is:", principal

main()