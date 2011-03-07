# Chapter:		11
# Exercise:		6
# Start:		06:44:54 PM 07/06/2007
# End:			06:50:00 PM 07/06/2007
# Rating:		3
# Note:			Shows how to write a random shuffler
from random import randrange

def Lshuffle(myList):
	newl = []
	while len(myList) > 0:
		ran = randrange(0, len(myList))
		newl.append(myList.pop(ran))
	return newl
		

def main():
	l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print l
	print Lshuffle(l)
	

main()
