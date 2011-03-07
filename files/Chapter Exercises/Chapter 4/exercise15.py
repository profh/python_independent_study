# Chapter:	4
# Exercise:	15
# Start:	07:52:08 PM 06/10/2007
# End:		07:54:47 PM 06/10/2007
# Rating:	4
# Note:		shows file access, string splitting...etc
import os
def main():
	filename = raw_input("Which file do you wish to analyze? ")
	if os.path.exists(filename):
		f = open(filename, "r")
		data = f.read()
		print "Total Characters:",str(len(data.replace("\n","").replace("\r","").replace("\t","")))
		print "Total Words:",str(len(data.split()))
		print "Total Lines:",str(data.count("\n"))
		print "Total Paragraphs:",str(data.count("\n\n"))
		
main()

