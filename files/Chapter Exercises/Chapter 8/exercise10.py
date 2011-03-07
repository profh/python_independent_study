# Chapter:		8
# Exercise:		10
# Start:		11:09:21 AM 06/25/2007
# End:			11:10:48 AM 06/25/2007
# Rating:		3
# Note:			Same as exercise 9, but with a file input

def main():
	infile = raw_input("What file to read for input? ")
	startodometer = 0
	
	f = open(infile, "r")
	curdistance = 0
	totalgas = 0
	count = 0
	for line in f:
		if count == 0:
			startodometer = int(line)
			count += 1
			continue
		temp = line.split()
		if (len(temp) != 2):
			continue
		odoreading = int(temp[0])
		gasused = int(temp[1])
		curdistance += odoreading-startodometer
		startodometer = odoreading
		totalgas += gasused
		
	print "MPG was",(float(curdistance)/float(totalgas))
	print "Total distance was",curdistance
	print "Total Gas usage was",totalgas
	f.close()

	
main()
