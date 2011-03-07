# Chapter:	3
# Exercise:	1
# Start:	03:45:00 PM 06/05/2007
# End:		03:48:48 PM 06/05/2007
# Rating:	3
# Note:		Use of math library.  forced to realize that math.pi is a constant, not a function.
import math
def main():
	print "This program calculates the volume and the area of a sphere"
	print "based on the given radius\n"
	radius = input("What is the radius of the sphere? ")
	volume = (4/3) * math.pi * math.pow(radius, 3)
	area = 4 * math.pi * math.pow(radius, 2)
	print "The volume of a sphere with a radius of",radius,"is",volume
	print "The area of a sphere with a radius of",radius,"is",area
	
main()