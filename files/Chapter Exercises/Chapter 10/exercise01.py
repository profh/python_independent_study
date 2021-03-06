# Chapter:		10
# Exercise:		1
# Start:		01:32:43 AM 07/01/2007
# End:			01:34:43 AM 07/01/2007
# Rating:		3
# Note:			adding a method to a class

# cball3.py
#   Simulation of the flight of a cannon ball (or other projectile)
#   Illustrates use of a class/object to organize data

from math import pi, sin, cos

class Projectile:

	def __init__(self, angle, velocity, height):
		self.xpos = 0.0
		self.ypos = height
		self.maxy = 0.0
		radians = pi * angle / 180.0
		self.xvel = velocity * cos(radians)
		self.yvel = velocity * sin(radians)
	
	def update(self, time):
		self.xpos = self.xpos + time * self.xvel
		yvel1 = self.yvel - 9.8 * time
		self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
		self.yvel = yvel1
		if (self.maxy < self.ypos):
			self.maxy = self.ypos
	
	def getMax(self):
		return self.maxy
	
	def getY(self):
		return self.ypos
	
	def getX(self):
		return self.xpos
	
def getInputs():
    a = input("Enter the launch angle (in degrees): ")
    v = input("Enter the initial velocity (in meters/sec): ")
    h = input("Enter the initial height (in meters): ")
    t = input("Enter the time interval between position calculations: ")
    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
		cball.update(time)        
    print "\nDistance traveled: %0.1f meters." % (cball.getX())
    print "Maximum Height achieved: %0.1f meters." % (cball.getMax())

main()

