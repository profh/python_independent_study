# Chapter:	2
# Exercise:	3
# Start:		03:06:02 PM 06/04/2007
# End:		03:07:55 PM 06/04/2007
# Rating:		2
# Note:		Shows loop logic with existing code

def main():
	for i in range(5):
		print "Temperature conversion #" + str(i+1) + "\r\n"
		celsius = input("What is the Celsius temperature? ")
		fahrenheit = 9.0 / 5.0 * celsius + 32
		print "The temperature is", fahrenheit, "degrees Fahrenheit."
		
main()
