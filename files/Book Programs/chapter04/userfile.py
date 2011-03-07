# userfile.py
#    Program to create a file of usernames in batch mode.

import string

def main():
    print "This program creates a file of usernames from a"
    print "file of names."

    # get the file names
    infileName = raw_input("What file are the names in? ")
    outfileName = raw_input("What file should the usernames go in? ")

    # open the files
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = string.split(line)
        # create a username
        uname = string.lower(first[0]+last[:7])
        # write it to the output file
        outfile.write(uname+'\n')

    # close both files
    infile.close()
    outfile.close()

    print "Usernames have been written to", outfileName

main()
