# Chapter:	3
# Exercise:	10
# Start:	05:01:07 PM 06/05/2007
# End:		05:03:37 PM 06/05/2007
# Rating:	3
# Note:		Math library functions (sin)
import math
def main():
	print "This program determines the length of a ladder required to reach a certain height when leaned against a house"
	print ""
	angle_deg = input("What is the angle of the ladder (in degrees)? ")
	angle_rad = (math.pi/180) * angle_deg
	
	height = input("What is the height of the ladder? ")
	length = (height/math.sin(angle_rad))
	
	print "Ladder need to have a length of",length,"to reach a height of",height

main()