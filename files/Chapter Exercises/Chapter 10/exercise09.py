# Chapter:		10
# Exercise:		9
# Start:		02:24:45 AM 07/01/2007
# End:			02:26:54 AM 07/01/2007
# Rating:		3
# Note:			shows use of self variables
import math

class SolidSphere:
	def __init__(self, radius):
		self.radius = radius
		
	def getRadius(self):
		return self.radius
		
	def surfaceArea(self):
		return 4.0 * math.pi * math.pow(self.radius, 2)

	def volume(self):
		return (4.0/3.0) * math.pi * math.pow(self.radius, 3)
	

def main():
	s = SolidSphere(10)
	print "Radius:",s.getRadius()
	print "Surface Area:",s.surfaceArea()
	print "Volume:",s.volume()


main()
