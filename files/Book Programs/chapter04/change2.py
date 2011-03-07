# change2.py
#   A program to calculate the value of some change in dollars.
#   This version representes the total cash in cents.


def main():
    print "Change Counter"
    print
    print "Please enter the count of each coin type."
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickels = input("Nickels: ")
    pennies = input("Pennies: ")
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies 
    print
    print "The total value of your change is $%d.%02d" \
          % (total/100, total%100)

main()

