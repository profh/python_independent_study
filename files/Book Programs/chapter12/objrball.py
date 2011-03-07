# objrrball.py
#    Simulation of a racquet game.
#    Illustrates design with objects.

from random import random

class Player:
    # A Player keeps track of service probability and score

    def __init__(self, prob):
        # Create a player with this probability
        self.prob = prob
        self.score = 0

    def winsServe(self):
        # RETURNS true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a point to this player's score
        self.score = self.score + 1

    def getScore(self):
        # RETURN this player's current score
        return self.score

class RBallGame:
    # A RBallGame represents a game in progress. A game as two players
    # and keeps track of which one is currently serving.

    def __init__(self, probA, probB):
        # Create a new game having players with the given probs.
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA  # Player A always serves first

    def play(self):
        # Play the game to completion
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()
            
    def isOver(self):
        # RETURNS game is finished (i.e. one of the players has won).
        a,b = self.getScores()
        return a == 15 or b == 15 or \
               (a == 7 and b == 0) or (b==7 and a == 0)

    def changeServer(self):
        # Switch which player is serving
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getScores(self):
        # RETURNS the current scores of player A and player B
        return self.playerA.getScore(), self.playerB.getScore()

class SimStats:
    # SimStatistics handles accumulation of statistics across multiple
    #   (completed) games. This version tracks the wins and shutouts for
    #   each player.

    def __init__(self):
        # Create a new accumulator for a series of games
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0

    def update(self, aGame):
        # Determine the outcome if aGame and update statistics
        a, b = aGame.getScores()
        
        if a > b:                             # A won the game
            self.winsA = self.winsA + 1
            if b == 0:
                self.shutsA = self.shutsA + 1
        else:                                 # B won the game
            self.winsB = self.winsB + 1
            if a == 0:
                self.shutsB = self.shutsB + 1

    def printReport(self):
        # Print a nicely formatted report
        n = self.winsA + self.winsB
        print "Summary of", n , "games:"
        print
        print "          wins (% total)   shutouts (% wins)  "
        print "--------------------------------------------"
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n)
        
    def printLine(self, label, wins, shuts, n):
        template = "Player %s:  %4d %5.1f%% %11d  %s"
        if wins == 0:        # Avoid division by zero!
            shutStr = "-----"
        else:
            shutStr = "%4.1f%%" % (float(shuts)/wins*100)
        print template % (label, wins, float(wins)/n*100, shuts, shutStr) 

def printIntro():
    print "This program simulates games of racquetball between two"
    print 'players called "A" and "B".  The ability of each player is'
    print "indicated by a probability (a number between 0 and 1) that"
    print "the player wins the point when serving. Player A always"
    print "has the first serve.\n"
        
def getInputs():
    # Returns the three simulation parameters
    a = input("What is the prob. player A wins a serve? ")
    b = input("What is the prob. player B wins a serve? ")
    n = input("How many games to simulate? ")
    return a, b, n

def main():
    printIntro()
    
    probA, probB, n = getInputs()

    # Play the games
    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB) # create a new game
        theGame.play()                    # play it
        stats.update(theGame)             # get info about completed game

    # Print the results
    stats.printReport()

if __name__ == "__main__":
    main()
    raw_input("\nPress <Enter> to quit")

