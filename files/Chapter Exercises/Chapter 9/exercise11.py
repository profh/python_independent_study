# Chapter:		9
# Exercise:		11
# Start:		01:01:52 AM 07/01/2007
# End:			01:05:27 AM 07/01/2007
# Rating:		3
# Note:			shows boolean logic

from random import randrange

def getRoll():
	return randrange(1,7)

def roll5dice():
	die1 = getRoll()
	die2 = getRoll()
	die3 = getRoll()
	die4 = getRoll()
	die5 = getRoll()
	if (die1 == die2 and die2 == die3 and die3 == die4 and die4 == die5 and die5 == die1):
		return 1
	else:
		return 0

def main():
	n = input("How many times to roll dice? ")
	total = 0
	for i in range(n):
		total += roll5dice()
	print "5 matching numbers appeared",total,"times",float(total)/n*100,"%"


main()
