# Chapter:		6
# Exercise:		11
# Start:		10:41:00 AM 06/18/2007
# End:			10:43:09 AM 06/18/2007
# Rating:		3
# Note:			Shows how to use functions to modify variables via return

def squareEach(nums):
	newnums = []
	for num in nums:
		newnums.append(num*num)
	return newnums

def main():
	nums = [2, 4, 6, 8, 10, 12, 14]
	
	for num in nums:
		print str(num)+"\t",
	print
	
	nums = squareEach(nums)

	for num in nums:
		print str(num)+"\t",
	print
	

main()