# Chapter:		8
# Exercise:		11
# Start:		11:14:06 AM 06/25/2007
# End:			11:17:02 AM 06/25/2007
# Rating:		2
# Note:			Easy exercise that just splits user input data

def main():
	temps = raw_input("Input average daily temperatures separated by spaces:\n")
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
