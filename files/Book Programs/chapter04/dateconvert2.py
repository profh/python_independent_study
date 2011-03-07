# dateconvert2.py
#    Converts day month and year numbers into two date formats

import string

def main():
    # get the day month and year
    day, month, year = input("Please enter day, month, year: ")

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = monthStr + " " + str(day) + ", " + str(year)

    print "The date is", date1, "or", date2

main()

