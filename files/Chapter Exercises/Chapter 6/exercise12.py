# Chapter:		6
# Exercise:		12
# Start:		10:45:01 AM 06/18/2007
# End:			10:46:11 AM 06/18/2007
# Rating:		3
# Note:			Shows how to use variables. No code reuse...finally

def sumList(nums):
	sum = 0.0
	for num in nums:
		sum += num
	return sum

def main():
	nums = [1,2,3,4,5,6,7,8,9,10]
	print "Sum of list is: %d\r\n"%sumList(nums)

main()
