# Chapter:		11
# Exercise:		15
# Start:		08:56:17 PM 07/06/2007
# End:			09:25:53 PM 07/06/2007
# Rating:		4
# Note:			Something useful for a change

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
			outstr = "A"
		elif self.rank == 11:
			outstr = "J"
		elif self.rank == 12:
			outstr = "Q"
		elif self.rank == 13:
			outstr = "K"
		else:		
			outstr = str(self.rank)
		
		if self.suit == "d":
			outstr = outstr + "D"
		elif self.suit == "c":
			outstr = outstr + "C"
		elif self.suit == "h":
			outstr = outstr + "H"
		elif self.suit == "s":
			outstr = outstr + "S"
		return outstr
		

class Deck:
	def __init__(self):
		self.cards = []
		self.__initdeck()
	
	def __initdeck(self):
		for i in range(1, 14):
			self.cards.append(Card(i, "d"))
			self.cards.append(Card(i, "c"))
			self.cards.append(Card(i, "h"))
			self.cards.append(Card(i, "s"))
		self.shuffle()
	
	def dealCard(self):
		if len(self.cards) > 0:
			return self.cards.pop()
		else:
			return None
	
	def cardsLeft(self):
		return len(self.cards)
	
	def shuffle(self):
		self.cards = self.Lshuffle(self.cards)
	
	def Lshuffle(self, myList):
		newl = []
		while len(myList) > 0:
			ran = randrange(0, len(myList))
			newl.append(myList.pop(ran))
		return newl
		
	
	def __str__(self):
		outstr = "["
		for i in range(0, len(self.cards)):
			if i == 0:
				outstr += str(self.cards[i])
			else:
				outstr += ", " + str(self.cards[i])
		outstr += "]"
		return outstr;
	
def main():
	d = Deck()
	while d.cardsLeft() > 0:
		print d.dealCard(),
	

main()
