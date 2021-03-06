# Chapter:		11
# Exercise:		1
# Start:		05:56:57 PM 07/06/2007
# End:			05:58:59 PM 07/06/2007
# Rating:		1
# Note:			I have no idea why this is an exercise

from math import sqrt

def getNumbers():
    nums = []     # start with an empty list

    # sentinel loop to get numbers
    xStr = raw_input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)   # add this value to the list
        xStr = raw_input("Enter a number (<Enter> to quit) >> ")
    return nums
    
def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)
    
def stdDev(nums, xbar=None):
    if xbar == None:
        xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))
def meanStdDev(nums):
	return self.mean(nums), self.stdDev(nums)


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size / 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos-1]) / 2.0
    else:
        median = nums[midPos]
    return median

def main():
    print 'This program computes mean, median and standard deviation.'

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)
    
    print '\nThe mean is', xbar
    print 'The standard deviation is', std
    print 'The median is', med

if __name__ == '__main__': main()
