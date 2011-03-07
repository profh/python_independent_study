# Chapter:	2
# Exercise:	5
# Start:		03:16:38 PM 06/04/2007
# End:		03:18:07 PM 06/04/2007
# Rating:		2
# Note:		shows that loop vars can be changed based on user input

def main():
	print "This program calculates the future value of a X-year investment."
	years = input("Enter the amount of years for this investment: ")

	principal = input("Enter the initial principal: ")
	apr = input("Enter the annual interest rate: ")

	for i in range(years):
		principal = principal * (1 + apr)

	print "The value in", years, "years is:", principal

main()