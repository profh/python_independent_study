# Chapter:	4
# Exercise:	14
# Start:	01/01/2008
# End:		01/01/2008
# Rating:	3.5
# Note:		shows file access


def main():
	print "This program illustrates a chaotic function"

	# get chaos inputs
	c = open("ex14data.txt", "r")
	x = float(c.readline().strip())
	y = float(c.readline().strip())

	# open file for output
	ofile = open("output.txt", "w")

	ofile.write("x is "+str(x)+"\n") 
	ofile.write("y is "+str(y)+"\n")
	ofile.write("\n\n")
	
	ofile.write("index\t"+str(x)+"\t"+str(y)+"\n")
	ofile.write("-----------------------------\n")
	
	for i in range(10):
		x = 3.9 * x * (1 - x)
		y = 3.9 * y * (1 - y)
		ofile.write(str(i)+"\t"+str(round(x,6))+"\t"+str(round(y,6))+"\n")


main()
