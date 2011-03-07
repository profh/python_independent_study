# Chapter:	3
# Exercise:	15
# Start:	05:18:16 PM 06/05/2007
# End:		05:22:43 PM 06/05/2007
# Rating:	3
# Note:		Deals with loops and types
import math

def main():
	print "This program approximates pi by summing a series of a length determined by the user"
	print ""
	n = input("How long should the sequence be? ")
	
	sum = float(0)
	
	
	for i in range(1,n*2,4):
		sum += (4.0/i)-(4.0/(i+2))
	
	print "Estimated pi is",sum
	print "Difference between math library and estimated pi is",(math.pi-sum)

main()