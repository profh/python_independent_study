# Chapter:		7
# Exercise:		18
# Start:		11:41:59 AM 06/21/2007
# End:			11:46:04 AM 06/21/2007
# Rating:		2
# Note:			Code reuse....
from graphics import *

def toNumbers(strList):
	newnums = []
	for snum in strList:
		try:
			newnums.append(int(snum))
		except ValueError:
			print snum,"is an invalid number. Skipping..."
		except AttributeError:
			print snum,"is an invalid number. Skipping..."
	return newnums

def main():
	testlist = (1, 2, "3", 4, 5, 6, 7, "3", "g", GraphWin("test", 200, 200))
	newlist = toNumbers(testlist)
	
main()
