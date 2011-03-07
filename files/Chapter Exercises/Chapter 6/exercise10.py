# Chapter:		6
# Exercise:		10
# Start:		10:38:57 AM 06/18/2007
# End:			10:40:32 AM 06/18/2007
# Rating:		3
# Note:			Shows how you can return more than a number. (You can return anything including strings)

def acronymize(instr):
	words = instr.split()
	outstr = ""
	for word in words:
		outstr = outstr + word[0].upper() + "." + " "
	
	return outstr



def main():
	fullword = raw_input("Type in words to acronymize: ")
	print acronymize(fullword)
	
main()
