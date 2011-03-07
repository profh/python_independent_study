# Chapter:		6
# Exercise:		3
# Start:		06:00:08 PM 06/17/2007
# End:			06:01:36 PM 06/17/2007
# Rating:		3
# Note:			Shows use of functions and return variables
import math

def sphereArea(radius):
	return 4 * math.pi * math.pow(radius, 2)

def sphereVolume(radius):
	return (4/3) * math.pi * math.pow(radius, 3)

def main():
	print "This program calculates the volume and the area of a sphere"
	print "based on the given radius\n"
	radius = input("What is the radius of the sphere? ")
	volume = sphereVolume(radius)
	area = sphereArea(radius)
	print "The volume of a sphere with a radius of",radius,"is",volume
	print "The area of a sphere with a radius of",radius,"is",area
main()