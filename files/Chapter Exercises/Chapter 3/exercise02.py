# Chapter:	3
# Exercise:	2
# Start:	03:51:13 PM 06/05/2007
# End:		03:55:16 PM 06/05/2007
# Rating:	2
# Note:		More math problems....
import math
def main():
	print "This program calculates the cost per square inch of a circular pizza"
	print "given its diameter and price"
	print ""
	diameter = input("What is the diameter of the pizza in inches? ")
	price = input("What is the price of the pizza? ")
	
	area = math.pi * math.pow(diameter, 2)
	
	costpersquareinch = price / area
	
	print "The cost per Square inch for this pizza is $",round(costpersquareinch,2)



main()
