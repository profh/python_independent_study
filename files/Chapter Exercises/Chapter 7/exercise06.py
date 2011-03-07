# Chapter:		7
# Exercise:		6
# Start:		10:45:41 AM 06/21/2007
# End:			10:48:15 AM 06/21/2007
# Rating:		3
# Note:			Good, if the user does the test to see if the input data works

def main():
	limit = input("What is the speed limit? ")
	speed = input("What was the clocked speed? ")
	if (speed - limit > 0):
		total = 50.0
		
		total += 5.0 * (speed - limit)
		
		if speed > 90:
			total += 200
		
		print "Total ticket price: $",total
	else:
		print "Clocked speed was within speed limit"
main()
