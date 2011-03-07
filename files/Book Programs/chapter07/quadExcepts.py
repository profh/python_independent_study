# quadratic6.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates robust exception handling to avoid crash on bad inputs

import math 

def main():
    print "This program finds the real solutions to a quadratic\n"

    try:
        a, b, c = input("Please enter the coefficients (a, b, c): ")
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print "\nThe solutions are:", root1, root2 
    except ValueError, excObj:
        msg = str(excObj)
        if msg == "math domain error":
            print "No Real Roots"
        elif msg == "unpack tuple of wrong size":
            print "You didn't give me the right number of coefficients!"
        else:
            print "Something went wrong, sorry!"
    except NameError:
        print "\nYou didn't enter three numbers"
    except TypeError:
        print "\nYour inputs were not all numbers"
    except SyntaxError:
        print "\nYour input was not in the correct form. Missing comma(s), perhaps?"
    ## except:
##         print 
##         print "\nSomething went wrong, sorry!"

if __name__ == '__main__':
    main()
