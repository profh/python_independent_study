# Chapter:		8
# Exercise:		4
# Start:		10:41:04 AM 06/25/2007
# End:			10:43:20 AM 06/25/2007
# Rating:		3
# Note:			shows looping with function with else/ifs
def syr(x):
	if (x%2 == 0):
		return x/2
	else:
		return 3*x + 1

def main():
	startnum = input("What is the starting number? ")
	while startnum != 1:
		print startnum,
		startnum = syr(startnum)
	print 1
main()
