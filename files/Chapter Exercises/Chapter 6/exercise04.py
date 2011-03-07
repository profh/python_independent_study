# Chapter:		6
# Exercise:		4
# Start:		06:03:07 PM 06/17/2007
# End:			06:06:02 PM 06/17/2007
# Rating:		2
# Note:			resue of old code.
import math

def sumN(n):
	sum = 0
	for i in range(1,n+1):
		sum += i
	return sum
def sumNCubes(n):
	sum = 0
	for i in range(1,n+1):
		sum += int(math.pow(i, 3))
	return sum

def main():
	n = input("What is n? ")
	print "The sum of the first",n,"numbers is:",sumN(n)
	print "The sum of the first",n,"cubes is:",sumNCubes(n)
main()
