# Chapter:		9
# Exercise:		4
# Start:		12:12:55 AM 07/01/2007
# End:			12:14:59 AM 07/01/2007
# Rating:		3
# Note:			the same thing...again


from random import random

def main():
    printIntro()
    probA, probB, n= getInputs()
    winsA, winsB= simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    # Prints an introduction to the program
    print "This program simulates a game of volleybal between two"
    print 'players called "A" and "B".  The abilities of each player is'
    print "indicated by a probability (a number between 0 and 1) that"
    print "the player wins the point when serving. Player A always"
    print "has the first serve.\n"

def getInputs():
    # RETURNS probA, probB, number of games to simulate
    a = input("What is the prob. player A wins a serve? ")
    b = input("What is the prob. player B wins a serve? ")
    n = input("How many games to simulate? ")
    return a, b, n

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
		rand = random()
		if rand < probA:
			scoreA = scoreA + 1
		else:
			scoreB = scoreB + 1
	return scoreA, scoreB

def gameOver(a,b):
    # a and b are scores for players in a racquetball game
    # RETURNS true if game is over, false otherwise
    return (a >= 30 or b >= 30) and (abs(a-b) > 1)

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print "\nGames simulated:", n
    print "Wins for A: %d (%0.1f%%)" % (winsA, float(winsA)/n*100)
    print "Wins for B: %d (%0.1f%%)" % (winsB, float(winsB)/n*100)

if __name__ == "__main__": main()

