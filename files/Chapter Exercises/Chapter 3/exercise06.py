# Chapter:	3
# Exercise:	6
# Start:	04:41:53 PM 06/05/2007
# End:		04:45:24 PM 06/05/2007
# Rating:	3
# Note:		More user inputs than usual (4)

def main():
	print "This program takes in 2 points and calculates the slope"
	print ""
	x1,y1 = input("Coordinates for point 1: x, y separated by a comma: ")
	x2,y2 = input("Coordinates for point 2: x, y separated by a comma: ")
	
	slope = (y2 - y1)/(x2-x1)
	
	print "The slope of ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+") is",slope 

main()