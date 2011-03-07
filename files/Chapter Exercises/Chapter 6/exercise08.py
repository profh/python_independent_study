# Chapter:		6
# Exercise:		8
# Start:		10:32:34 AM 06/18/2007
# End:			10:36:02 AM 06/18/2007
# Rating:		1
# Note:			Code Reuse from chapter 3....again....

import math

def nextGuess(guess, x):
	print "Next Guess: %d is %0.6f"%(guess, x)

def main():
	print "This program guesses the square root of a number using the newtonian method"
	print ""
	num = input("What is the number that you want the square root of? ")
	guess = 0
	
	tolerance = 0.000001
	
	if num == 0:
		guess = 0
	else:
		x = abs(num)
		while True:
			nx = 0.5 * (x + (num / x))
			nextGuess(nx, x)
			if abs(x - nx) < tolerance:
				break
			x = nx
		guess = nx
	
	
	print "The guess is",guess
	print "The math.sqrt is",math.sqrt(num)
	print "The difference is",(math.sqrt(num)-guess)

main()