#This program will generate a pretty HTML file containing the notes and stuff for each chapter and exercise

import os
import re
import time
import math

def getfiles(path):
	exercises = []
	os.chdir(path)
	for entry in os.listdir(path):
		if os.path.isdir(entry):
			for exercise in os.listdir(path + entry):
				exercises.append(entry + "/" + exercise)
	return exercises
	
def duration(timestamp):
	years = math.floor(timestamp / (60*60*24*365))
	timestamp%=60*60*24*365
	weeks=math.floor(timestamp / (60*60*24*7))
	timestamp%=60*60*24*7
	days=math.floor(timestamp / (60*60*24))
	timestamp%=60*60*24
	hrs=math.floor(timestamp / (60*60))
	timestamp%=60*60
	mins=math.floor(timestamp / 60)
	secs=timestamp % 60;
	
	out = ""
	if (years >= 1):
		out += str(int(years)) + " year" + plural(years) + " "
	if (weeks >= 1):
		out += str(int(weeks)) + " week" + plural(weeks) + " "
	if (days >= 1):
		out += str(int(days)) + " day" + plural(days) + " "
	if (hrs >= 1):
		out += str(int(hrs)) + " hour" + plural(hrs) + " "
	if (mins >= 1):
		out += str(int(mins)) + " minute" + plural(mins) + " "
	if (secs >= 1):
		out += str(int(secs)) + " second" + plural(secs)
	
	return out
	

def plural(num):
	if num != 1:
		return "s"
	else:
		return ""
def main():
	#create output file
	print "\r\n"
	out_file = open("notes.html", "w")
	out_file.write("<html>\n<head>\n<title>Python Programs</title>\n</head>\n<body>\n<table border='1'>")
	out_file.write("\n<thead>\n<tr><th>Chapter</th><th>Exercise</th><th>Duration</th><th>Rating</th><th>Notes</th></tr>\n</thead>\n<tbody>\n")
	filelocation = "C:/Users/Ari Rubinstein/Documents/Cmu/Summer 2007/Python/Chapter Exercises/"
	exercisefiles = getfiles(filelocation);
	for file in exercisefiles:
		# Chapter:	2
		# Exercise:	1
		# Start:		1:26 PM 6/4/2007
		# End:		1:28 PM 6/4/2007
		# Rating:		2
		# Note:		Simple program...demonstrates printing out a line of code
		
		curfile = open("./"+file)
		
		p = re.compile("^.*Chapter:\t(.*)$")
		m = p.match(curfile.readline())
		chapter = m.group(1)
		
		p = re.compile("^.*Exercise:\t(.*)$")
		m = p.match(curfile.readline())
		exercisenum = m.group(1)

		p = re.compile("^.*Start:\t\t(.*)$")
		m = p.match(curfile.readline())
		starttime = m.group(1)

		p = re.compile("^.*End:\t\t(.*)$")
		m = p.match(curfile.readline())
		endtime = m.group(1)

		p = re.compile("^.*Rating:\t\t(.*)$")
		m = p.match(curfile.readline())
		rating = m.group(1)

		p = re.compile("^.*Note:\t\t(.*)$")
		m = p.match(curfile.readline())
		note = m.group(1)

		out_file.write("<tr>")
		out_file.write("<td>"+chapter+"</td>")
		out_file.write("<td>"+exercisenum+"</td>")
		
		timestring = "%I:%M:%S %p %m/%d/%Y"
		
		
		startt = time.mktime(time.strptime(starttime, timestring))
		endt = time.mktime(time.strptime(endtime, timestring))
		dur = duration(endt-startt);
		
		out_file.write("<td>"+dur+"</td>")		
		if rating == "1":
			out_file.write("<td align='center' bgcolor='#FF687C'>")
		elif rating == "2":
			out_file.write("<td align='center' bgcolor='#FF8C33'>")
		elif rating == "3":
			out_file.write("<td align='center' bgcolor='#FFF04D'>")
		elif rating == "4":
			out_file.write("<td align='center' bgcolor='#B2FF3E'>")

		out_file.write(rating+"</td>")
		out_file.write("<td>"+note+"</td>")
		out_file.write("</tr>")
		
	print "\r\n"
	out_file.write("</tbody>\n</table>\n</body>\n</html>")
	out_file.close();

main()




def readfile(filename):
	#open file
	curfile = open(filename, "r")
	
