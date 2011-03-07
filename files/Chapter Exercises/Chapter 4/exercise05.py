# Chapter:	4
# Exercise:	5
# Start:	07:17:49 PM 06/10/2007
# End:		07:19:39 PM 06/10/2007
# Rating:	3
# Note:		shows that the word is actually an array 

def main():
	fullword = raw_input("Type in words to acronymize: ")
	words = fullword.split()
	for word in words:
		print word[0].upper() + ".",
	print ""


main()