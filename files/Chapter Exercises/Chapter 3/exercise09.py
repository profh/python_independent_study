# Chapter:	3
# Exercise:	9
# Start:	04:57:39 PM 06/05/2007
# End:		04:59:44 PM 06/05/2007
# Rating:	2
# Note:		Uses math library. Nothing special. Pushes that primitives are not callable objects
import math
def main():
	print "This program will calculate the area of a triangle given the"
	print " length of the three sides"
	print ""
	a = input("Enter Side 1: ")
	b = input("Enter Side 2: ")
	c = input("Enter Side 3: ")
	
	s = (a+b+c)/2
	A = math.sqrt(s * (s - a)*(s - b)*(s - c))
	
	print "The Area of the triangle is",A
	

main()