# Chapter:		8
# Exercise:		6
# Start:		10:47:10 AM 06/25/2007
# End:			10:50:49 AM 06/25/2007
# Rating:		3
# Note:			loops previous program

import math
def isprime(cur):
	for num in range(2, int(math.sqrt(cur))):
		if (cur%num == 0):
			print cur,"is not a prime number"
			return
	print cur,"is a prime number"
				

def main():
	n = input("Find primes from 2 till? ")
	for cur in range(2, n):
		isprime(cur)
main()
