# Chapter:		8
# Exercise:		2
# Start:		10:32:48 AM 06/25/2007
# End:			10:35:58 AM 06/25/2007
# Rating:		3
# Note:			Shows print formatting again

def calculate(T, V):
	return 35.74 + 0.6215 * T - 35.75*(V**0.16) + 0.4275 * T * (V**0.16)

def main():
	for windspeed in range(0, 50, 5):
		print "%2d | "%windspeed,
		for temp in range(-20, 60, 10):
			print "% 2.3f "% calculate(temp, windspeed),
		print

main()
