# Chapter:		10
# Exercise:		11
# Start:		02:30:41 AM 07/01/2007
# End:			02:38:11 AM 07/01/2007
# Rating:		4
# Note:			Shows data storage and methods within a class
from random import randrange

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
	n = input("Number of cards to generate? ")
	for i in range(n):
		c = Card(randrange(1, 14), randsuit())
		print c," - Blackjack Value",c.BJValue()
		
main()
