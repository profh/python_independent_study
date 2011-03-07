# Chapter:		8
# Exercise:		9
# Start:		11:01:27 AM 06/25/2007
# End:			11:08:59 AM 06/25/2007
# Rating:		3
# Note:			continuous user input

def main():
	startodometer = input("What is the starting odometer reading? ")
	curdistance = 0
	totalgas = 0
	while True:
		instr = raw_input("Enter in odometer reading and amount of gas used separated by a space:\n")
		temp = instr.split()
		if len(temp) != 2:
			break;
		odoreading = int(temp[0])
		gasused = int(temp[1])
		
		curdistance += odoreading-startodometer
		startodometer = odoreading
		totalgas += gasused
		
	print "MPG was",(float(curdistance)/float(totalgas))
	print "Total distance was",curdistance
	print "Total Gas usage was",totalgas
	

	
main()
