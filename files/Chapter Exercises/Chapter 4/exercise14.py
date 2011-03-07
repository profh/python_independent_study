# Chapter:	4
# Exercise:	14
# Start:	07:49:17 PM 06/10/2007
# End:		07:50:44 PM 06/10/2007
# Rating:	3
# Note:		shows file access

def main():
    print "This program illustrates a chaotic function"
    c = open("ex14data.txt", "r")
    x = float(c.readline().strip())
    y = float(c.readline().strip())
    print "x is",x
    print "y is",y
    
    print "index\t"+str(x)+"\t"+str(y)
    print "-----------------------------"
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print str(i) + "\t" + str(round(x, 6)) + "\t" + str(round(y, 6))

main()
