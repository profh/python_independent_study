# Chapter:		8
# Exercise:		1
# Start:		10:26:24 AM 06/25/2007
# End:			10:27:11 AM 06/25/2007
# Rating:		2
# Note:			Dupe of exercise 16, chapter 3

import math

def main():
	print "This program calculates a fibonacci sequence with a user supplied n"
	print ""
	n = input("What is n? ")
	
	num1 = 1
	num2 = 1
	next = 0
	
	for i in range(1,n):
		next = num1+num2
		num1 = num2
		num2 = next
	
	print "Number is",num1

main()
