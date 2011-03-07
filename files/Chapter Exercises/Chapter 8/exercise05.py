# Chapter:		8
# Exercise:		5
# Start:		10:43:37 AM 06/25/2007
# End:			10:45:55 AM 06/25/2007
# Rating:		2
# Note:			shows looping with for and range
import math
def main():
	n = input("Input a number to see if it is prime: ")
	for num in range(2, int(math.sqrt(n))):
		if (n%num == 0):
			print n,"is not a prime number"
			return
	
	print n,"is a prime number"
main()
