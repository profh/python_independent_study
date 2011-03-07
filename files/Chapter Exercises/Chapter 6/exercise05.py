# Chapter:		6
# Exercise:		5
# Start:		10:19:32 AM 06/18/2007
# End:			10:21:34 AM 06/18/2007
# Rating:		2
# Note:			Bad Problem.  Just fixing an old one with functions
import math

def CostPerSquareInch(price, area):
	return price / area


def AreaOfPizza(diameter):
	return math.pi * math.pow(diameter, 2)


def main():
	print "This program calculates the cost per square inch of a circular pizza"
	print "given its diameter and price"
	print ""
	diameter = input("What is the diameter of the pizza in inches? ")
	price = input("What is the price of the pizza? ")
	print "The cost per Square inch for this pizza is $",round(CostPerSquareInch(price,AreaOfPizza(diameter)),2)


main()
