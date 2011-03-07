# username.py
#    Simple string processing program to generate usernames. 

def main():
    print "This program generates computer usernames."
    print

    # get user's first and last names
    first = raw_input("Please enter your first name (all lowercase): ")
    last = raw_input("Please enter your last name (all lowercase): ")

    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]

    # output the username
    print "Your username is:", uname

main()
