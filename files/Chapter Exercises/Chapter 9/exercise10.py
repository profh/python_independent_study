# Chapter:		9
# Exercise:		10
# Start:		12:57:16 AM 07/01/2007
# End:			01:01:25 AM 07/01/2007
# Rating:		3
# Note:			Shows cool way to calculate pi
from random import random
def main():
	h=0
	n = input("How many darts to throw? ")
	for i in range(n):
		x = 2*random()-1
		y = 2*random()-1
		if x**2 + y**2 <= 1:
			#inside circle
			h+= 1
	pi = 4.0 * (float(h)/float(n))
	print "Estimated Pi is",pi

main()

	
	