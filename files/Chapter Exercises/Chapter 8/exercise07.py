# Chapter:		8
# Exercise:		7
# Start:		10:50:57 AM 06/25/2007
# End:			10:57:04 AM 06/25/2007
# Rating:		4
# Note:			Shows nested loops
import math
def isprime(cur):
	for num in range(2, int(math.sqrt(cur))):
		if (cur%num == 0):
			return False
	return True
def generateprimes(upperlimit):
	outlist = []
	for n in range(2, upperlimit):
		if isprime(n):
			outlist.append(n)
	return outlist
	
def iseven(n):
	if n%2 == 0:
		return True
	else:
		return False

def main():
	num = input("Please input a number: ")
	if (iseven(num)):
		print num,"is even"
		for x in generateprimes(num):
			for y in generateprimes(num):
				if x + y == num:
					print x,"+",y,"==",num
		
	else:
		print num,"is not even"

main()
