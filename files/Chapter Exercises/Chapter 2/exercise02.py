# Chapter:	2
# Exercise:	2
# Start:		03:03:23 PM 06/04/2007
# End:		03:03:59 PM 06/04/2007
# Rating:		2
# Note:		Shows how input can take in multiple variables in one shot

def main():
    print "This program computes the average of two exam scores."
    print

    score1, score2, score3 = input("Enter three scores separated by a commas: ")
    average = (score1 + score2 + score3) / 3.0

    print "The average of the scores is:", average

main()
