# Chapter:	3
# Exercise:	14
# Start:	05:16:48 PM 06/05/2007
# End:		05:19:34 PM 06/05/2007
# Rating:	4
# Note:		Shows what you can do within the loop and that the user can determine how many times something will be done. I copied code from exercise 13.

def main():
	print "This program averages a series of numbers inputted by the users"
	print ""
	n = input("How many numbers would you wish to average up? ")
	sum = 0.0
	for i in range(1,n+1):
		cur = input("Entry #"+str(i)+": ")
		sum += cur
	average = sum/n
	
	print "The average of your",n,"numbers is",average


main()