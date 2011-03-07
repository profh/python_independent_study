# Chapter:	4
# Exercise:	8
# Start:	07:29:05 PM 06/10/2007
# End:		07:30:31 PM 06/10/2007
# Rating:	3
# Note:		Shows use of chr and ord

def main():
	shift = input("How many characters to shift by? ")
	words = raw_input("What do you want to encode? ")
	newstr = ""
	for word in words.strip():
		newstr = newstr + chr(ord(word) + shift)
	
	print "Encoded String: " + newstr
	
	
	

main()
