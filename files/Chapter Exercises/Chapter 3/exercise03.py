# Chapter:	3
# Exercise:	3
# Start:	03:58:00 PM 06/05/2007
# End:		04:02:29 PM 06/05/2007
# Rating:	3
# Note:		Fun to do (relative to the other exercises) 

def main():
	H_weight = 1.0079
	C_weight = 12.011
	O_weight = 15.9994
	print "This program will determine the molecular weight of a hydrocarbon"
	print "based on the number of hydrogen, carbon, and oxygen atoms present"
	print ""
	num_H = input("How many Hydrogen Atoms? ")
	num_C = input("How many Carbon Atoms? ")
	num_O = input("How many Oxygen Atoms? ")
	sum = (num_H * H_weight) + (num_C * C_weight) + (num_O * O_weight)
	print "The sum of your hydrocarbon (H:" + str(num_H) + ", C:" + str(num_C) + ", O:" + str(num_O) + ") is",sum
	

main()