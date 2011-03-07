# Chapter:	3
# Exercise:	12
# Start:	05:09:19 PM 06/05/2007
# End:		05:10:48 PM 06/05/2007
# Rating:	3
# Note:		Uses a loop and refrences a variable outside. forces use of math.pow and math lib

import math
def main():
	print "This program finds the sum of the cubes of the first n natural numbers (provided by user)"
	print ""
	n = input("You want the sum of how many cubes of natural numbers? ")
	sum = 0
	for i in range(1,n+1):
		sum += int(math.pow(i, 3))
	
	print "The sum of the cubes natural numbers starting at 1 till",n,"is",sum
	

main()