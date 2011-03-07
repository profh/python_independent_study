# Chapter:		6
# Exercise:		7
# Start:		10:30:18 AM 06/18/2007
# End:			10:32:06 AM 06/18/2007
# Rating:		2
# Note:			Shows return args
import math
def fib(n):
	num1 = 1
	num2 = 1
	next = 0
	
	for i in range(1,n):
		next = num1+num2
		num1 = num2
		num2 = next
	
	return num1


def main():
	print "This program calculates a fibonacci sequence with a user supplied n"
	print ""
	n = input("What is n? ")
	
	
	print "Number is",fib(n)
	
	
	

main()