# Chapter:		11
# Exercise:		11
# Start:		07:08:14 PM 07/06/2007
# End:			07:13:23 PM 07/06/2007
# Rating:		3
# Note:			Theres a million ways to do this, but whatever

def main():
	badwords = ["shit", "poop", "piss", "damn", "fuck"]
	filename = raw_input("File to censor: ")
	f = open(filename, "r")
	for line in f:
		for word in badwords:
			replacewith = ""
			for i in range(0, len(word)):
				replacewith = replacewith + "*"
			line = line.replace(word, replacewith)
		print line
	

	f.close()

main()
