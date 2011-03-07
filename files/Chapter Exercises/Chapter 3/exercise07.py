# Chapter:	3
# Exercise:	7
# Start:	04:48:33 PM 06/05/2007
# End:		04:50:09 PM 06/05/2007
# Rating:	2
# Note:		Just like exercise 6.  Lots of code reuse. Just uses the math library
import math
def main():
	print "This program takes in 2 points and calculates the distance"
	print ""
	x1,y1 = input("Coordinates for point 1: x, y separated by a comma: ")
	x2,y2 = input("Coordinates for point 2: x, y separated by a comma: ")

	distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
	
	print "The distance between ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+") is",distance

main()