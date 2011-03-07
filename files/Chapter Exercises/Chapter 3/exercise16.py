# Chapter:	3
# Exercise:	16
# Start:	05:30:41 PM 06/05/2007
# End:		05:42:43 PM 06/05/2007
# Rating:	3
# Note:		Had to remember how to do fib sequence non-recursively
import math

def main():
	print "This program calculates a fibonacci sequence with a user supplied n"
	print ""
	n = input("What is n? ")
	
	num1 = 1
	num2 = 0
	next = 0
	
	for i in range(1,n+1):
		next = num1+num2
		num1 = num2
		num2 = next
		print "%d => %d" % (i, num1)
	
	print "Number for %d is %d" % (n, num1)
	
	
	

main()