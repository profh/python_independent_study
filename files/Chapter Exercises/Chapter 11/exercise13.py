# Chapter:		11
# Exercise:		13
# Start:		07:15:04 PM 07/06/2007
# End:			07:22:54 PM 07/06/2007
# Rating:		3
# Note:			Simple sorting if you realize that there are 52 cards in the deck

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
	def getDeckValue(self):
		tot = self.rank
		if self.suit == "d":
			tot = tot + 0
		elif self.suit == "c":
			tot = tot + (13*1)
		elif self.suit == "h":
			tot = tot + (13*2)
		elif self.suit == "s":
			tot = tot + (13*3)
		return tot
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
		
def cmpCards(c1, c2):
	return cmp(c1.getDeckValue(), c2.getDeckValue())
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
	infile = "cards.txt"
	f = open(infile, "r")
	cards = []
	for s in f:
		info = s.split()
		c = Card(int(info[0]), info[1])
		cards.append(c)
	f.close()
	for s in cards:
		print s
	cards.sort(cmpCards)
	print
	for s in cards:
		print s
	
main()	