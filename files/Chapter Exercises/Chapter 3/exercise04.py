# Chapter:	3
# Exercise:	4
# Start:	04:09:19 PM 06/05/2007
# End:		04:14:40 PM 06/05/2007
# Rating:	2
# Note:		More math...

def main():
	print "This program will determine the distance to a lightning strike"
	print "based on the time elapsed between the flash and the sound of thunder"
	print ""
	seconds = input("How many seconds later did the thunder appear after the flash? ")
	distance = seconds / (5280.0/1100.0)
	print "The lightning strike was",distance,"miles away"
	

main()