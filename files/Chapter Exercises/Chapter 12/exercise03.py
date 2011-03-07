# Chapter:		12
# Exercise:		3
# Start:		10:00:55 PM 07/30/2007
# End:			11:05:29 PM 07/30/2007
# Rating:		4
# Note:			Shows how to create a database
import os
class Attendee:
	def __init__(self, name, company, state, email):
		self.name = name
		self.company = company
		self.state = state
		self.email = email
		self.deleted = False
		self.idnum = -1
	def filestr(self):
		return str(self.idnum) + "\t" + self.name + "\t" + self.company + "\t" + self.state + "\t" + self.email
	def name(self):
		return self.name
	def company(self):
		return self.company
	def state(self):
		return self.state
	def email(self):
		return self.email
	def idnum(self):
		return self.idnum
	def cmpID(self, idnumin):
		if self.idnum == idnumin:
			return True
		else:
			return False
	
	def setid(self, idnum):
		self.idnum = idnum
		
	def __str__(self):
		return "#"+str(self.idnum)+": " + self.name + " ("+self.company+", "+self.state+"): "+ self.email
	
	def isState(self, inval):
		if (inval.lower() == self.state.lower()):
			return True
		else:
			return False
	def delete(self):
		self.deleted = True
	
	def getNameEmail(self):
		return self.name + ": " + self.email
		
	def isDeleted(self):
		return self.deleted		

class Conference:
	def __init__(self):
		self.attendees = []
		self.databasefile = "attendees.txt"
		self.clearScreen()
		self.openfile()

	def cmpName(s1, s2):
		return cmp(s1.name(), s2.name())

	def clearScreen(self):
		print "\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n"

	def addAttendee(self, attendee, id):
		attendee.setid(id)
		self.attendees.append(attendee)
		self.attendees.sort()
			
		print "Added attendee #"+str(id),
		print ":", attendee
		print
		
	def getAttendeeIndex(self, attendeeID):
		for i in range(0, len(self.attendees)):
			if self.attendees[i].idnum == attendeeID and self.attendees[i].isDeleted() == False:
				return i
		return -1
	
	
	def nextid(self):
		highestnum = 0
		for i in self.attendees:
			num = i.idnum
			if num > highestnum:
				highestnum = num
		return highestnum + 1
		
	def printMenu(self):
		print
		print "Main Menu"
		print "1) Add an Attendee ..."
		print "2) Get Info on Attendee Number ___"
		print "3) Delete Attendee Number ___"
		print "4) List All Attendees"
		print "5) List Names and Email Adreesses of all Attendees"
		print "6) List Names and Email Adreesses of all Attendees in State ___"
		print "7) Quit (and save database)"
		print "---------------------------------------------------------------"
		
	def openfile(self):
		if (os.path.exists(self.databasefile)):
			f = open(self.databasefile, "r")
			for line in f.readlines():
				data = line.strip().split("|", 4)
				if (len(data) == 5):
					a = Attendee(data[1].strip(), data[2].strip(), data[3].strip(), data[4].strip())
					a.setid(int(data[0].strip()))
					self.attendees.append(a)
			f.close()
			print "Loaded",str(len(self.attendees)),"attendees from database file"
		else:
			print "Unable to load database.  Starting from scratch"
	
	def savefile(self):
		f = open(self.databasefile, "w")
		for i in self.attendees:
			if not i.isDeleted():
				f.write(i.filestr() + "\n")
		f.close()
				
	
	def DoEvents(self):
		while True:
			self.printMenu()
			choice = input("Please Select a choice: ")
			if (choice < 1 or choice > 7):
				print "Invalid Choice"
				print
				continue
			
			self.clearScreen()
			
			if choice == 1:
				name = raw_input("Attendee's Name: ")
				company = raw_input("Attendee's Company: ")
				state = raw_input("Attendee's State: ")
				email = raw_input("Attendee's Email Address: ")
				a = Attendee(name, company, state, email)
				self.addAttendee(a, self.nextid())
			elif choice == 2:
				idnum = input("Attendee's ID Number: ")
				num = self.getAttendeeIndex(idnum)
				if num == -1:
					print "Error: Could not find attendee #",idnum
					print
				else:
					print self.attendees[num]
			elif choice == 3:
				idnum = input("Attendee's ID Number: ")
				num = self.getAttendeeIndex(idnum)
				if num == -1:
					print "Error: Could not find attendee #",idnum
					print
				else:
					self.attendees[num].delete()
					print "Attendee #"+str(idnum)+" deleted"
					print
			elif choice == 4:
				for i in self.attendees:
					if not i.isDeleted():
						print i
				print
			elif choice == 5:
				for i in self.attendees:
					if not i.isDeleted():
						print i.getNameEmail()
				print
			elif choice == 6:
				state = raw_input("State to search for: ")
				for i in self.attendees:
					if not i.isDeleted() and i.isState(state):
						print i.getNameEmail()
			elif choice == 7:
				self.savefile()
				return
			
		

def main():
	c = Conference()
	c.DoEvents()
	
main()

	
