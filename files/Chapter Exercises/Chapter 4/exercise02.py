# Chapter:	4
# Exercise:	2
# Start:	10:42:34 AM 06/06/2007
# End:		10:44:35 AM 06/06/2007
# Rating:	4
# Note:		Shows use of string printing formatting


import string

def main():
    # get the day month and year
    day, month, year = input("Please enter day, month, year: ")

    date1 = "%d/%d/%d" % (month, day, year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = "%s %d, %d" % (monthStr, day, year)

    print "The date is %s or %s" % (date1, date2)

main()

