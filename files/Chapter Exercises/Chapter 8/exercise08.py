# Chapter:		8
# Exercise:		8
# Start:		10:57:16 AM 06/25/2007
# End:			11:01:11 AM 06/25/2007
# Rating:		2
# Note:			weird to understand formula
def gcd(n,m):
	while m != 0:
		t = m
		m = n % m
		n = t
	return n


def main():
	print "GCD of 24/4 is",gcd(24,4)

main()
