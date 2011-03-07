# Chapter:	3
# Exercise:	17
# Start:	05:43:29 PM 06/05/2007
# End:		05:49:03 PM 06/05/2007
# Rating:	3
# Note:		Difficult due to the algorithm.  Have we learned while loops yet?
import math

def main():
	print "This program guesses the square root of a number using the newtonian method"
	print ""
	num = input("What is the number that you want the square root of? ")
	guess = 0
	
	tolerance = 0.000001
	
	if num == 0:
		guess = 0
	else:
		t = abs(num)
		while True:
			newt = 0.5 * (t + (num / t))
			if abs(t - newt) < tolerance:
				break
			t = newt
		guess = newt
	
	
	print "The guess is",guess
	print "The math.sqrt is",math.sqrt(num)
	print "The difference is",(math.sqrt(num)-guess)

main()