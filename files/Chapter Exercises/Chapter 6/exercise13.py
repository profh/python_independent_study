# Chapter:		6
# Exercise:		13
# Start:		10:46:41 AM 06/18/2007
# End:			10:48:30 AM 06/18/2007
# Rating:		3
# Note:			Shows use of Data Types and how you can mass-convert.  Buuuut..without a try/catch, these methods are useless

def toNumbers(strList):
	newnums = []
	for snum in strList:
		newnums.append(int(snum))
	return newnums

def main():
	strList = ["1","2","3","4","5","6"]
	
	for num in strList:
		print num + "\t",
	print

	numList = toNumbers(strList)
	
	for num in numList:
		print str(num) + "\t",
	print


main()
