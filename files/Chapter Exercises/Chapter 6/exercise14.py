# Chapter:		6
# Exercise:		14
# Start:		10:56:39 AM 06/18/2007
# End:			11:03:25 AM 06/18/2007
# Rating:		4
# Note:			The ultimate worst code reuse: from current other exercises in the chapter!!!  shows reading in from a file

def sumList(nums):
	sum = 0.0
	for num in nums:
		sum += num
	return sum

def toNumbers(strList):
	newnums = []
	for snum in strList:
		newnums.append(int(snum))
	return newnums

def squareEach(nums):
	newnums = []
	for num in nums:
		newnums.append(num*num)
	return newnums

def printList(list):
	for item in list:
		print str(item) + "\t",
	print
	
def main():
	inputfilename = "ex14data.txt"
	nums = []
	f = open(inputfilename, "r")
	for line in f:
		line = line.strip()
		nums.append(line)
	f.close
	
	print "List of strings: "
	printList(nums)
	
	nums = toNumbers(nums)
	print "List of Numbers: "
	printList(nums)
	
	print "Sum of numbers: " + str(sumList(nums))
	print
	print "Squaring Each Number..."
	squares = squareEach(nums)
	printList(squares)


main()