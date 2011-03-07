# Chapter:	4
# Exercise:	9
# Start:	07:32:37 PM 06/10/2007
# End:		07:35:15 PM 06/10/2007
# Rating:	3
# Note:		deals with chr and ord

def main():
	shift = input("How many characters to shift by? ")
	words = raw_input("What do you want to encode? ")
	newstr = ""
	for word in words.strip():
		num = ord(word) + shift
		if num > 122:
			num = num - 57
		elif num < 65:
			num = num + 57
		
		newstr = newstr + chr(num)
	
	print "Encoded String: "+newstr
	
	
	

main()
