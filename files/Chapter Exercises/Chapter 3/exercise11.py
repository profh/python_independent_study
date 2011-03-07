# Chapter:	3
# Exercise:	11
# Start:	05:04:45 PM 06/05/2007
# End:		05:07:45 PM 06/05/2007
# Rating:	3
# Note:		Uses a loop and refrences a variable outside

def main():
	print "This program finds the sum of the first n natural numbers (provided by user)"
	print ""
	n = input("You want the sum of how many natural numbers? ")
	sum = 0
	for i in range(1,n+1):
		sum += i
	
	print "The sum of natural numbers starting at 1 till",n,"is",sum
	

main()