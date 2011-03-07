# Chapter:	4
# Exercise:	13
# Start:	07:45:53 PM 06/10/2007
# End:		07:47:33 PM 06/10/2007
# Rating:	2
# Note:		Looping an old program
def main():
	print "This program calculates the future value of a 10-year investment."

	principal = input("Enter the initial principal: ")
	apr = input("Enter the annual interest rate: ")
	num = input("How many years for the investment: ")

	for i in range(num):
		principal = principal * (1 + apr)
		print "%i\t$%d" % (i, principal)

	print "The value in",num,"years is:", principal
main()