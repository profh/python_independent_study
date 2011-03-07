# printfile.py
#     Prints a file to the screen.

def main():
    fname = raw_input("Enter filename: ")
    infile = open(fname,'r')
    data = infile.read()
    print data

main()
