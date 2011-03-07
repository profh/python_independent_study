# Chapter:	4
# Exercise:	1
# Start:	10:35:56 AM 06/06/2007
# End:		10:36:52 AM 06/06/2007
# Rating:	3
# Note:		Shows use of string split/join

import string  # include string library for the split function.

def main():
    print "This program converts a sequence of ASCII numbers into"
    print "the string of text that it represents."
    print
    
    # Get the message to encode
    inString = raw_input("Please enter the ASCII-encoded message: ")

    # Loop through each substring and build ASCII message
    msgList = []
    for numStr in string.split(inString):
        # convert the (sub)string to a number
        asciiNum = eval(numStr)
        # append character to message
        msgList.append(chr(asciiNum))
	message = string.join(msgList, "")
	
    print "The decoded message is:", message

main()
