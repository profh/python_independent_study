# Chapter:		9
# Exercise:		2
# Start:		11:59:50 PM 06/30/2007
# End:			12:02:59 AM 07/01/2007
# Rating:		2
# Note:			hard to understand question


from random import random

def main():
    printIntro()
    probA, probB, n, bestofn= getInputs()
    winsA, winsB, shutouta, shutoutb = simBestOfNGames(probA, probB, n, bestofn)
    printSummary(winsA, winsB, shutouta, shutoutb)

def printIntro():
    # Prints an introduction to the program
    print "This program simulates a game of racquetball between two"
    print 'players called "A" and "B".  The abilities of each player is'
    print "indicated by a probability (a number between 0 and 1) that"
    print "the player wins the point when serving. Player A always"
    print "has the first serve.\n"

def getInputs():
    # RETURNS probA, probB, number of games to simulate
    a = input("What is the prob. player A wins a serve? ")
    b = input("What is the prob. player B wins a serve? ")
    n = input("How many games to simulate? ")
    bestofn = input("Number of matched per game? ")
    return a, b, n, bestofn

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players A and B
    # RETURNS number of wins for A, number of wins for B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def simBestOfNGames(probA, probB, n, bestofn):
	wina = 0
	winb = 0
	shutouta = 0
	shutoutb = 0
	for i in range(n):
		tempa, tempb = simNGames(bestofn, probA, probB)
		if tempa != 0 and tempb == 0:
			shutouta += 1
		elif tempa == 0 and tempb != 0:
			shutoutb += 1
		wina += tempa
		winb += tempb
	
	return wina, winb, shutouta, shutoutb

def gameOver(a,b):
    # a and b are scores for players in a racquetball game
    # RETURNS true if game is over, false otherwise
    return a == 15 or b == 15

def printSummary(winsA, winsB, shutouta, shutoutb):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print "\nGames simulated:", n
    print "Wins for A: %d (%0.1f%%) - Shutouts: %d (%0.1f%%)" % (winsA, float(winsA)/n*100, shutouta, float(shutouta)/n*100)
    print "Wins for B: %d (%0.1f%%) - Shutouts: %d (%0.1f%%)" % (winsB, float(winsB)/n*100, shutoutb, float(shutoutb)/n*100)

if __name__ == "__main__": main()





