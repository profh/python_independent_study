# Chapter:		12
# Exercise:		1
# Start:		08:50:59 PM 07/30/2007
# End:			10:00:24 PM 07/30/2007
# Rating:		4
# Note:			Shows how to modify existing programs

import os
from graphics import *
from button import Button
from cdieview import ColorDieView
from dice import Dice
class HighScores:
	def __init__(self):
		self.filename = "highscores.txt"
		self.scorerequirement = 101
		
	def getHighScores(self):
		
		if (not os.path.exists(self.filename)):
			return -1
		else:
			scores = []
			f = open(self.filename, "r")
			for line in f:
				score = line.split("\t")
				if len(score) == 2:
					scores.append(score)
			f.close()
			return scores
	
	def isElgible(self, score):
		if score >= self.scorerequirement:
			return True
		else:
			return False
	
	def addToList(self, score, name):
		f = open(self.filename, "a")
		f.write(str(score) + "\t" + name + "\n")
		f.close()
	
	

class PokerApp:

	def __init__(self, interface):
		self.dice = Dice()
		self.money = 100
		self.interface = interface
	def processScore(self, score):
		h = HighScores()
		if h.isElgible(score):
			nameentry = GraphWin("Name Entry", 200, 100)
			entry = Entry(Point(50, 50), 10)
			entry.draw(nameentry)
			okbutton = Button(nameentry, Point(150, 50), 90, 50, "Save Name")
			okbutton.activate()
			while 1:
				m = nameentry.getMouse()
				if okbutton.clicked(m):
					h.addToList(score, entry.getText())
					nameentry.close()
					return
	
	def run(self):
		while self.money >= 10:
			result = self.interface.wantToPlay()
			if result == "Roll Dice":
				self.playRound()           
			elif result == "Help":
				h = HelpScreen()
				h.DoEvents()
			elif result == "Quit":
				self.processScore(self.money)
				break
		self.interface.close()
	
	def playRound(self):
		self.money = self.money - 10
		self.interface.setMoney(self.money)
		self.doRolls()
		result, score = self.dice.score()
		self.interface.showResult(result, score)
		self.money = self.money + score
		self.interface.setMoney(self.money)        

	def doRolls(self):
		self.dice.rollAll()
		roll = 1
		self.interface.setDice(self.dice.values())
		toRoll = self.interface.chooseDice()
		while roll < 3 and toRoll != []:
			self.dice.roll(toRoll)
			roll = roll + 1
			self.interface.setDice(self.dice.values())
			if roll < 3:
				toRoll = self.interface.chooseDice()


class SplashScreen:
	def __init__(self):
		self.win = GraphWin("Dice Poker", 600, 500)
		self.win.setBackground("white");
		banner = Text(Point(300,30), "Python  Poker  Parlor")
		banner.setSize(24)
		banner.setFill("black")
		banner.setStyle("bold")
		banner.draw(self.win)
		info = Text(Point(300, 60), "This program allows a user to play video poker using dice")
		info.setFill("black")
		info.draw(self.win)
		self.letsplaybutton = Button(self.win, Point(200, 100), 180, 40, "Let's Play")
		self.letsplaybutton.activate()
		self.exitbutton = Button(self.win, Point(400, 100), 180, 40, "Exit")
		self.exitbutton.activate()
		
		highscorebanner = Text(Point(300, 150), "High Scores")
		highscorebanner.setSize(24)
		highscorebanner.setFill("black")
		highscorebanner.setStyle("bold")
		highscorebanner.draw(self.win)
		highscores = HighScores()
		scores = highscores.getHighScores()
		
		if (scores == -1):
			Text(Point(300, 180), "No High Scores Available").draw(self.win)
		else:
			for i in range(0, len(scores)):
				
				Text(Point(300, 200 + (20 * i)), scores[i][1].strip() + ": " + str(scores[i][0]).strip()).draw(self.win)
		
		
	def DoEvents(self):
		while True:
			m = self.win.getMouse()
			if self.letsplaybutton.clicked(m):
				return "Play"
			elif self.exitbutton.clicked(m):
				return "Exit"
	def destroy(self):
		self.win.close()
	


class HelpScreen:
	def __init__(self):
		self.win = GraphWin("Dice Poker Help", 600, 450)
		self.win.setBackground("white");
		banner = Text(Point(300,30), "Python  Poker  Parlor Help")
		banner.setSize(24)
		banner.setFill("black")
		banner.setStyle("bold")
		banner.draw(self.win)
		info = Text(Point(300, 60), "This program allows a user to play video poker using dice")
		info.setFill("black")
		info.draw(self.win)
		text = [
		"* The player starts with $100                             ",
		"* Each round costs $10 to play.  This amount is subtracted",
		"  from the user's money at the start of the round         ",
		"* The player initially rolls a completely random hand     ",
		"  (i.e. all five dice are rolled)                         ",
		"* The player gets two chances to enhance the hand by      ",
		"  rerolling some or all of the dice                       ",
		"* At the end of the hand, the player's money is updated   ",
		"  according to the following payout schedule:             ",
		"  Hand                                       Pay          ",
		" ---------------------------------------------------------",
		"  Two Pairs                                  $5           ",
		"  Three of a Kind                            $8           ",
		"  Full House (A Pair and a Three of a kind)  $12          ",
		"  Four of a Kind                             $15          ",
		"  Straight (1-5 or 2-6)                      $20          ",
		"  Five of a Kind                             $30          "
		]
		for i in range(0, len(text)):
			startheight = 80
			
			t = Text(Point(300, startheight+(20 * i)), text[i])
			t.setFace("courier")
			t.draw(self.win)
		
		self.closebutton = Button(self.win, Point(550, 350), 50, 40, "Close")
		self.closebutton.activate()
		
	def DoEvents(self):
		while True:
			m = self.win.getMouse()
			if self.closebutton.clicked(m):
				self.win.close()
				return


	
	
class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the dice table.")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(520, 375), 40, 30, "Help")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
        
    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die %d" % (i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def choose(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while 1:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def setMoney(self, amt):
        self.money.setText("$%d" % (amt))

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Help", "Quit"])
        self.msg.setText("")
        return ans

    def close(self):
        self.win.close()

    def showResult(self, msg, score):
        if score > 0:
            text = "%s! You win $%d" % (msg, score)
        else:
            text = "You rolled %s" % (msg)
        self.msg.setText(text)

    def chooseDice(self):
        choices = []
        while 1:
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score"])
            if b[0] == "D":
                i = eval(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices
    

splash = SplashScreen()
if splash.DoEvents() == "Play":
	splash.destroy()
	inter = GraphicsInterface()
	app = PokerApp(inter)
	app.run()
else:
	splash.destroy()



