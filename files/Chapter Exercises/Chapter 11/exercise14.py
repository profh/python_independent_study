# Chapter:		11
# Exercise:		14
# Start:		07:23:36 PM 07/06/2007
# End:			07:55:28 PM 07/06/2007
# Rating:		4
# Note:			Difficult, but might be cool to do a rand generator to see likelyhoods of getting certain hands

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
def cmpRanks(c1, c2):
	return cmp(c1.getRank(), c2.getRank())
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
def isInList(myList, x):
	for i in myList:
		if i == x:
			return True
	return False
def samesuits(cards):
	if ((cards[0].getSuit() == cards[1].getSuit()) and (cards[1].getSuit() == cards[2].getSuit()) and (cards[2].getSuit() == cards[3].getSuit()) and (cards[3].getSuit() == cards[4].getSuit()) and (cards[4].getSuit() == cards[0].getSuit())):
		return True
	return False
def getlowest(cards):
	lowest = 100
	for s in cards:
		if s.getRank() < lowest:
			lowest = s.getRank()
	return lowest
def gethighest(cards):
	highest = 0
	for s in cards:
		if s.getRank() > highest:
			highest = s.getRank()
	return highest
	
def isStraight(cards):
	cards.sort(cmpRanks)
	if gethighest(cards)-getlowest(cards) == 4:
		if cards[0].getRank()+1 == cards[1].getRank() and cards[1].getRank()+1 == cards[2].getRank() and cards[2].getRank()+1 == cards[3].getRank() and cards[3].getRank()+1 == cards[4].getRank():
			return True
	return False
			

def analyzeCards(cards):
	rankcount = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	suitcount = {"d":0, "c":0, "h":0, "s":0}
	
	cards.sort(cmpCards)
	
	for s in cards:
		rankcount[s.getRank()-1] = rankcount[s.getRank()-1] + 1
		suitcount[s.getSuit()] = suitcount[s.getSuit()] + 1
		
	if samesuits(cards) and rankcount[9] == 1 and rankcount[0] == 1 and rankcount[10] == 1 and rankcount[11] == 1 and rankcount[12] == 1:
		print "Royal Flush: 10, Jack, Queen, King, Ace, all of the same suit"
		return
		
	if isStraight(cards) and samesuits(cards):
		print "Straight Flush: Five ranks in a row, all of the same suit"
		return
		
	if isInList(rankcount, 4):
		print "Four of a Kind: Four of the same rank"
		return
		
	if isInList(rankcount, 3) and isInList(rankcount, 2):
		print "Full House: Three of one rank and two of another"
		return
		
	if samesuits(cards):
		print "Flush: Five cards of the same suit"
		return
		
	if isStraight(cards):
		print "Straight: Five ranks in a row"
		return
		
	if isInList(rankcount, 3):
		print "Three of a kind: Three of one rank"
		return
	
	if isInList(rankcount, 2) and (not isInList(rankcount, 1) and not isInList(rankcount, 3) and not isInList(rankcount, 4)):
		print "Two Pair: Two each of two different ranks"
		return
	
	if isInList(rankcount, 2):
		print "Pair: Two of the same rank"
		return
	
	cards.sort(cmpRanks)
	print "X High:",cards[4], cards[3]
	return
		
	
	

def main():
	#flush
	#cards = [Card(1, "d"), Card(2, "d"), Card(3, "d"), Card(4, "d"),Card(5, "d")]
	#4 or a kind
	#cards = [Card(1, "d"), Card(1, "c"), Card(1, "h"), Card(1, "s"),Card(5, "d")]
	#full house
	cards = []
	for i in range(100):
		cards = [Card(randrange(1,14),randsuit()),Card(randrange(1,14),randsuit()),Card(randrange(1,14),randsuit()),Card(randrange(1,14),randsuit()),Card(randrange(1,14),randsuit())]
		analyzeCards(cards)
	
main()