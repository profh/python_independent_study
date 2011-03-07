# Chapter:	3
# Exercise:	5
# Start:	04:15:55 PM 06/05/2007
# End:		04:19:24 PM 06/05/2007
# Rating:	3
# Note:		Shows reuse of variables

def main():
	print "This program calculates the cost of a coffee order"
	print ""
	pounds = input("How many pounds of coffee? ")
	
	cost_of_coffee = 10.50 * pounds
	cost_of_shipping = (0.86 * pounds) + 1.50
	
	print "The cost of the Coffee is $"+str(round(cost_of_coffee,2))
	print "The cost of shipping is $"+str(round(cost_of_shipping,2))
	print "The total cost of the order is $"+str(round(cost_of_coffee + cost_of_shipping, 2))

main()