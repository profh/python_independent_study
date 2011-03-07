# Chapter:	4
# Exercise:	6
# Start:	07:21:27 PM 06/10/2007
# End:		07:26:45 PM 06/10/2007
# Rating:	4
# Note:		shows use of string functions

def main():
	letters = raw_input("What is the name to calculate? ")
	charsum = 0
	for letter in letters.upper():
		if (letter.isalpha()):
			print letter
			charsum += (ord(letter)-64)

	print "Character Sum: " + str(charsum)


main()