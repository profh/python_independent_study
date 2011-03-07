# average7.py
#     Computes the average of numbers listed in a file.
#     Works with multiple numbers on a line.

import string

def main():
    fileName = raw_input("What file are the numbers in? ")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in string.split(line, ","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print "\nThe average of the numbers is", sum / count

if __name__ == '__main__':
    main()

