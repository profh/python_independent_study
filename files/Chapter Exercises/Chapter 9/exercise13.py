# Chapter:		9
# Exercise:		13
# Start:		01:12:23 AM 07/01/2007
# End:			01:15:43 AM 07/01/2007
# Rating:		3
# Note:			shows use of 4way random

from random import randrange


def main():
	n = input("How many steps? ")
	leftright = 0
	updown = 0
	for i in range(n):
		r = randrange(0,4)
		if r == 0:
			updown += 1
		elif r == 1:
			updown -= 1
		elif r == 2:
			leftright += 1
		elif r == 3:
			leftright -= 1
	print "Up/Down movement:",updown
	print "Left/Right movement:",leftright
	
main()
	


