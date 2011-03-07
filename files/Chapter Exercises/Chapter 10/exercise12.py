# Chapter:		10
# Exercise:		12
# Start:		02:42:38 AM 07/01/2007
# End:			02:50:18 AM 07/01/2007
# Rating:		4
# Note:			Really cool activity.  Shows use of images

from random import randrange
from graphics import *

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit.lower()
		
	def getRank(self):
		return self.rank
	def getSuit(self):
		return self.suit
	def BJValue(self):
		if self.rank > 10:
			return 10
		else:
			return self.rank
	
	def getImageString(self):
		outstr = self.suit
		if self.rank == 11:
			outstr = outstr + "j"
		elif self.rank == 12:
			outstr = outstr + "q"
		elif self.rank == 13:
			outstr = outstr + "k"
		else:
			outstr = outstr + str(self.rank)
		return outstr+".gif"
	
	def __str__(self):
		outstr = ""
		if self.rank == 1:
			outstr = "Ace"
		elif self.rank == 11:
			outstr = "Jack"
		elif self.rank == 12:
			outstr = "Queen"
		elif self.rank == 13:
			outstr = "King"
		else:		
			outstr = str(self.rank)
		outstr = outstr + " of "
		if self.suit == "d":
			outstr = outstr + "Diamonds"
		elif self.suit == "c":
			outstr = outstr + "Clubs"
		elif self.suit == "h":
			outstr = outstr + "Hearts"
		elif self.suit == "s":
			outstr = outstr + "Spades"
		return outstr
		
def randsuit():
	r = randrange(0, 4)
	if r == 0:
		return "d"
	elif r == 1:
		return "c"
	elif r == 2:
		return "h"
	elif r == 3:
		return "s"


def main():
	win = GraphWin("Random 5 card hand", 500, 200)
	win.setBackground("green2")

	for i in range(5):
		c = Card(randrange(1, 14), randsuit())
		print c
		print "cards/"+c.getImageString()
		im = Image(Point(50 + (100*i), 100), "cards/"+c.getImageString())
		im.draw(win)
	win.getMouse()
	win.close()
		
main()
