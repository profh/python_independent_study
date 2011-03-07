# Chapter:	4
# Exercise:	7
# Start:	07:21:27 PM 06/10/2007
# End:		07:26:45 PM 06/10/2007
# Rating:	4
# Note:		shows use of string functions. I don't see the difference between the last exercise and this one

def main():
	letters = raw_input("What is the name to calculate? ")
	charsum = 0
	for letter in letters.upper():
		if (letter.isalpha()):
			charsum += (ord(letter)-64)

	print "Character Sum: " + str(charsum)


main()