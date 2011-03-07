# Chapter:		7
# Exercise:		7
# Start:		10:49:07 AM 06/21/2007
# End:			10:54:17 AM 06/21/2007
# Rating:		2
# Note:			Weird hour question

def main():
	#assumed 24 hour time
	shour = input("Starting Hour (24 hour): ")
	smins = input("Starting Minute: ")
	ehour = input("Ending Hour (24 hour): ")
	emins = input("Ending Minute: ")
	total = 0.0
	if ehour >= (12+9):
		total += (((12+9)-shour) + (smins/60.0)) * 2.50
		total += ((ehour - (12+9)) + (emins/60.0)) * 1.75
	else:
		total += 2.50 * ((ehour-shour) + ((emins-smins)/60.0))
		
	print "Total Amount earned: $"+str(total)

main()
