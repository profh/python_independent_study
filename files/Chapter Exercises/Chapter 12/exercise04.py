# Chapter:		12
# Exercise:		4
# Start:		11:06:17 PM 07/30/2007
# End:			11:33:44 PM 07/30/2007
# Rating:		3
# Note:			Same thing as before

import os
class Account:
	def __init__(self, userid, pin):
		self.userid = userid
		self.pin = pin
		self.savingsamount = 0
		self.checkingamount = 0
	def setSavings(self, savingsvalue):
		self.savingsamount = savingsvalue
	def setChecking(self, checkingvalue):
		self.checkingamount = checkingvalue
	def getSavings(self):
		return self.savingsamount
	def getChecking(self):
		return self.checkingamount
	def filestring(self):
		return str(self.userid) + "|" + str(self.pin) + "|" + str(self.savingsamount) + "|" + str(self.checkingamount)


class ATM:
	def __init__(self):
		self.accounts = []
		self.databasefile = "accounts.txt"
		self.curaccount = -1
		self.clearScreen()
		self.openfile()
	def clearScreen(self):
		print "\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n"
	def openfile(self):
		if (os.path.exists(self.databasefile)):
			f = open(self.databasefile, "r")
			for line in f.readlines():
				data = line.strip().split("|", 3)
				if (len(data) == 4):
					a = Account(int(data[0].strip()), int(data[1].strip()))
					a.setSavings(float(data[2].strip()))
					a.setChecking(float(data[3].strip()))
					self.accounts.append(a)
			f.close()
			print "Loaded",str(len(self.accounts)),"accounts from database file"
		else:
			print "Unable to load database.  Starting from scratch"
	def savefile(self):
		f = open(self.databasefile, "w")
		for i in self.accounts:
			f.write(i.filestring() + "\n")
		f.close()
	
	def printMenu(self, menuid):
		if menuid == 1:
			print
			print "Login Menu"
			print "1) Log In"
			print "2) Quit (and save database)"
			print "---------------------------------------------------------------"
			
			choice = input("Choose: ")
			if (choice < 1 or choice > 2):
				self.printMenu(1)
				return
			if (choice == 1):
				userid = input("User ID: ")
				for i in range(0, len(self.accounts)):
					if self.accounts[i].userid == userid:
						pin = input("PIN: ")
						if self.accounts[i].pin == pin:
							self.curaccount = i
							
						else:
							print "Invalid PIN"
							self.printMenu(1)
				
			if (choice == 2):
				self.curaccount = -1
				self.savefile()
				return
			if self.curaccount != -1:
				self.printMenu(2)
							
		elif menuid == 2:
			print
			print "Main Menu"
			print "1) Balance of Checking"
			print "2) Balance of Savings"
			print "3) Deposit into Checking"
			print "4) Deposit into Savings"
			print "5) Transfer from Checking to Savings"
			print "6) Transfer from Savings to Checking"
			print "7) Log Out"
			print "---------------------------------------------------------------"
			choice = input("Choose: ")
			if (choice < 1 or choice > 7):
				self.printMenu(2)
				return
			acct = self.accounts[self.curaccount]
			if choice == 1:
				print "Checking Balance:",acct.getChecking()
			elif choice == 2:
				print "Savings Balance:",acct.getSavings()
			elif choice == 3:
				amount = input("Amount to deposit into checking: ")
				acct.setChecking(acct.getChecking() + amount)
			elif choice == 4:
				amount = input("Amount to deposit into savings: ")
				acct.setSavings(acct.getSavings() + amount)
			elif choice == 5:
				amount = input("Amount to transfer from Checking to Savings: ")
				acct.setChecking(acct.getChecking() - amount)
				acct.setSavings(acct.getSavings() + amount)
			elif choice == 6:
				amount = input("Amount to transfer from Savingsa to Checking: ")
				acct.setChecking(acct.getChecking() + amount)
				acct.setSavings(acct.getSavings() - amount)
			elif choice == 7:
				self.curaccount = -1
				self.printMenu(1)
				return
				
			self.printMenu(2)
			
			
		
	




def main():
	a = ATM()
	a.printMenu(1)
main()

















