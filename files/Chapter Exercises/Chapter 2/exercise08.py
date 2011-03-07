# Chapter:	2
# Exercise:	8
# Start:		03:27:17 PM 06/04/2007
# End:		03:31:35 PM 06/04/2007
# Rating:		3
# Note:		i had a bug.  needed to have the .0 to have the number not be an int.  Shows a little bit of typing


def main():
	print "This program will convert Fahrenheit temperature to Celcius."
	fahrenheit = input("What is the Fahrenheit temperature? ")
	celcius = (5.0/9.0)*(fahrenheit-32.0)
	print "The temperature is", celcius, "degrees celcius."
main()

