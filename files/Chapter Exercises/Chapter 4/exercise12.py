# Chapter:	4
# Exercise:	12
# Start:	07:41:21 PM 06/10/2007
# End:		07:43:43 PM 06/10/2007
# Rating:	2
# Note:		changing input vals

def main():
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    y = input("Enter a number between 0 and 1: ")
    print "index\t"+str(x)+"\t"+str(y)
    print "-----------------------------"
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print str(i) + "\t" + str(round(x, 6)) + "\t" + str(round(y, 6))

main()
