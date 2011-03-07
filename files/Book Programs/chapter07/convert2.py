# convert2.py
#      A program to convert Celsius temps to Fahrenheit.
#      This version issues heat and cold warnings.

def main():
    celsius = input("What is the Celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "The temperature is", fahrenheit, "degrees fahrenheit."
    if fahrenheit >= 90:
        print "It's really hot out there, be careful!"
    if fahrenheit <= 30:
        print "Brrrrr. Be sure to dress warmly"

main()

