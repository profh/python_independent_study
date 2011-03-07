# Chapter:	2
# Exercise:	4
# Start:		03:13:05 PM 06/04/2007
# End:		03:15:48 PM 06/04/2007
# Rating:		3
# Note:		shows how a loop variable can be used within the loop and how range takes more arguments

def main():
	for i in range(0, 100, 10):
		celsius = i
		fahrenheit = 9.0 / 5.0 * celsius + 32
		print "The temperature is", fahrenheit, "degrees Fahrenheit."

main()
