# Chapter:		10
# Exercise:		10
# Start:		02:27:29 AM 07/01/2007
# End:			02:29:54 AM 07/01/2007
# Rating:		3
# Note:			Shows use of self variables

class SolidCube:
	def __init__(self, sidelength):
		self.sidelength = sidelength
	
	def getSideLength(self):
		return self.sidelength
	
	def surfaceArea(self):
		return (self.sidelength * self.sidelength) * 6.0
		
	def volume(self):
		return self.sidelength * self.sidelength * self.sidelength
		
def main():
	s = SolidCube(10)
	print "Side Length:",s.getSideLength()
	print "Surface Area:",s.surfaceArea()
	print "Volume:",s.volume()


main()

	