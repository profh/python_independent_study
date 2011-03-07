# Chapter:	4
# Exercise:	11
# Start:	07:37:55 PM 06/10/2007
# End:		07:39:20 PM 06/10/2007
# Rating:	3
# Note:		String splitting

def main():
	sentence = raw_input("Please enter your sentence: ")
	numwords = len(sentence.split())
	chartotal = 0.0
	for word in sentence.split():
		chartotal += len(word)
	avglength = chartotal / numwords
	print "Average word length is ",avglength

main()