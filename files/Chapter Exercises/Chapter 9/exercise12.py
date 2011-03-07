# Chapter:		9
# Exercise:		12
# Start:		01:06:51 AM 07/01/2007
# End:			01:09:54 AM 07/01/2007
# Rating:		3
# Note:			shows returning of number
from random import randrange

def getDirection():
	if randrange(1,3) == 1:
		return 1
	else:
		return -1
		
def main():
	n = input("How many steps? ")
	dist = 0
	for i in range(n):
		dist += getDirection()
	print "Walk total distance was",dist

	

main()
