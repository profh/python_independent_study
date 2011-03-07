# Chapter:		9
# Exercise:		8
# Start:		12:36:03 AM 07/01/2007
# End:			12:51:09 AM 07/01/2007
# Rating:		4
# Note:			Shows how blackjack works

from random import randrange

def getRandomCardVal():
	num = randrange(1,14)
	if num > 10:
		num = 10
	return num
def isAce(num):
	if num == 1:
		return True
	return False

def runGame():
	dealercard1 = getRandomCardVal()
	dealercard2 = getRandomCardVal()
	total = dealercard1 + dealercard2
	if total == 21 or (isAce(dealercard1) and dealercard2 == 10) or (isAce(dealercard2) and dealercard1 == 10):
		return True
	
	
	while total < 17:
		newcard = getRandomCardVal()
		if isAce(newcard) and total >= 17 and total <= 21:
			total += 11
		else:
			total += newcard
	if total > 21:
		return False
	else:
		return True
	


def main():
	n = input("How many games to simulate? ")
	bustcount = 0
	for i in range(n):
		if not runGame():
			bustcount = bustcount + 1
	
	print "Total Bust Count:",bustcount," - ",float(bustcount)/(n) * 100,"%"
	
if __name__ == "__main__": main()

