# maxn.py
#    Finds the maximum of a series of numbers

def main():
    n = input("How many numbers are there? ")
    
    # Set max to be the first value
    max = input("Enter a number >> ")
    
    # Now compare the n-1 successive values
    for i in range(n-1): 
        x = input("Enter a number >> ")
        if x > max:
            max = x

    print "The largest value is", max

main()
