# Chapter:		7
# Exercise:		5
# Start:		10:41:56 AM 06/21/2007
# End:			10:44:52 AM 06/21/2007
# Rating:		2
# Note:			Simple if/else with sqrt
import math
def main():
	weight = float(input("What is your weight (in pounds)? "))
	height = float(input("What is your height (in inches)? "))
	bmi = weight / math.sqrt(height)
	
	if bmi >=19 and bmi <= 25:
		print "Your BMI (%d) is considered healthy" % bmi
	else:
		print "Your BMI (%d) is not considered healthy" % bmi

main()
