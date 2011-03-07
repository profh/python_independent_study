# Chapter:		11
# Exercise:		7
# Start:		06:50:23 PM 07/06/2007
# End:			06:52:24 PM 07/06/2007
# Rating:		2
# Note:			Quick and easy function

def innerProd(x, y):
	sum = 0
	for i in range(0, len(x)-1):
		sum += x[i]*y[i]
	return sum
def main():
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	y = [2, 3, 23, 45, 12, 13, 11, 50, 60]
	ip = innerProd(x, y)
	print ip
main()

	