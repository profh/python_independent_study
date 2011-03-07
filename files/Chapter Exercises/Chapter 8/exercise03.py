# Chapter:		8
# Exercise:		3
# Start:		10:36:16 AM 06/25/2007
# End:			10:39:59 AM 06/25/2007
# Rating:		3
# Note:			Shows looping through the year

def main():
	rate = input("What is the annual interest rate? ")
	princip = 1.0
	current = princip
	target = princip * 2
	curyear = 0
	while current < target:
		current += current * rate
		curyear += 1

	print "Investment will double in %d years at an annual rate of %0.2f"%(curyear, rate)
main()
