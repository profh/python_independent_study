# Chapter:		8
# Exercise:		12
# Start:		11:17:36 AM 06/25/2007
# End:			11:19:49 AM 06/25/2007
# Rating:		3
# Note:			same as exercise 11, but with a file input

def main():
	filename = raw_input("Filename for input data: ")
	
	f = open(filename, "r")
	temps = f.readline()
	f.close()
	
	coolingdays = 0
	heatingdays = 0
	for temp in temps.split():
		temp = int(temp)
		if temp < 60:
			coolingdays += 60-temp
		elif temp > 80:
			heatingdays += temp-80
	
	print "Total cooling days:",coolingdays
	print "Total heating days:",heatingdays
	

main()
