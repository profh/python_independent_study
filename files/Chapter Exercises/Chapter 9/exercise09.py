# Chapter:		9
# Exercise:		9
# Start:		12:53:20 AM 07/01/2007
# End:			12:56:50 AM 07/01/2007
# Rating:		2
# Note:			not much change from previous exercise

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

def runGame(startcard):
	dealercard1 = startcard
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
	for x in range(1, 11):
		bustcount = 0
		for i in range(n):
			if not runGame(x):
				bustcount = bustcount + 1
		print "Total busts for start card of",x,"was",bustcount,"-",float(bustcount)/n * 100, "%"
	
if __name__ == "__main__": main()

