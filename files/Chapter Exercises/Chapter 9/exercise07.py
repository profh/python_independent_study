# Chapter:		9
# Exercise:		7
# Start:		12:28:46 AM 07/01/2007
# End:			12:35:32 AM 07/01/2007
# Rating:		4
# Note:			They get to make their own game

from random import randrange

def simCrapsGame():
	die1 = randrange(1,7)
	die2 = randrange(1,7)
	total = die1 + die2
	initalval = total
	
	if total == 2 or total == 3 or total == 12:
		return 0
	else:
		while 1:
			die1 = randrange(1,7)
			die2 = randrange(1,7)
			total = die1 + die2
			if total == 7:
				return 0
			elif total == initalval:
				return 1
	
	
	
	

def main():
	print "This program simulates craps"
	n = input("How many games to simulate? ")
	score = 0
	for i in range(n):
		score += simCrapsGame()
	
	print "\nGames simulated:", n
	print "Wins: %d (%0.1f%%)" % (score, float(score)/n*100)
	




if __name__ == "__main__": main()
