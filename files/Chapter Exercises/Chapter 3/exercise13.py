# Chapter:	3
# Exercise:	13
# Start:	05:13:02 PM 06/05/2007
# End:		05:15:07 PM 06/05/2007
# Rating:	4
# Note:		Shows what you can do within the loop and that the user can determine how many times something will be done

def main():
	print "This program sums a series of numbers inputted by the users"
	print ""
	n = input("How many numbers would you wish to sum up? ")
	sum = 0
	for i in range(1,n+1):
		cur = input("Entry #"+str(i)+": ")
		sum += cur
	
	print "The sum of your",n,"numbers is",sum


main()