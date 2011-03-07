#This program will generate a pretty HTML file containing the notes and stuff for each chapter and exercise

import os, re, datetime, time, math, string, operator
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from mod_python import apache, psp

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


def getfiles(path):
	exercises = []
	os.chdir(path)
	for entry in os.listdir(path):
		exercises.append(entry)
	return exercises
	
def getchapters():
	path = "/var/www/html/python/files/Chapter Exercises/"
	chaps = []
	os.chdir(path)
	for entry in os.listdir(path):
		if os.path.isdir(entry):
			chaps.append(entry)
	chaps.sort()
	return chaps

def getBookPrograms():
	path = "/var/www/html/python/files/Book Programs/"
	chaps = []
	os.chdir(path)
	for entry in os.listdir(path):
		if os.path.isdir(entry):
			chaps.append(entry)
	chaps.sort()
	return chaps


def generateSideBarContent():
	sidebar = []
	chaps = []
	for chap in getchapters():
		chaps.append({"url": "chapter?chap=" + chap, "text": chap})
	links = []
	links.append({"url": "/python/static/references/2.5/index.html", "text": "Quick Reference (2.5) (HTML)"})
	links.append({"url": "/python/static/references/2.4/qr24.pdf", "text": "Quick Reference (2.4) (PDF)"})
	links.append({"url": "http://effbot.org/tkinterbook/", "text": "TKinter Reference (HTML)"})
	sidebar.append({"title":"Chapters", "itemlist":chaps})
	sidebar.append({"title":"Links", "itemlist":links})
	
	return sidebar

def displayPage(req, contentblocks, pagetitle = "Python Project 2007", sidebarblocks = generateSideBarContent(), show_code_css = False):
	curmicroseconds = datetime.datetime.now().microsecond
	req.content_type = 'text/html'
	t = psp.PSP(req, filename="templates/page.tmpl")
	t.run(vars = {"pagetitle": pagetitle, "sidebarblocks": sidebarblocks, "contentblocks": contentblocks, "show_code_css": show_code_css, "elapsedseconds": (math.pow(10, -6) * (datetime.datetime.now().microsecond-curmicroseconds))})
	return

def contentBlock(title = "", content = ""):
	return {"title": title, "content": content}

def chapter(req, chap = ''):
	if chap in getchapters():
		chapcontent = showChapter(req, chap)
		displayPage(req, [contentBlock(chap, chapcontent)])
	else:
		displayPage(req, [contentBlock("Error!", "There are no chapters available")])
	return

def index(req):
	displayPage(req, [contentBlock("Welcome!", "Welcome to the python project 2007.  You can view the book examples and chapter exercise archives by accessing the tabs near the top of the page. <br /> To get the clipboard functions to work, set signed.applets.codebase_principal_support = true in firefox's about:config")])
	return

def showChapter(req, chapter):
	relativepath = "/python/files/Chapter Exercises/" + str(chapter) + "/"
	fullpath = "/var/www/html"
	filelocation = fullpath + relativepath
	
	exercisefiles = getfiles(filelocation);
	exercises = []	
	exercisefiles.sort()
	for file in exercisefiles:
		if file[:8] != "exercise":
			continue;
		
		curfile = open("./"+file)
		contents = curfile.read()
		
		vals = {}
		for match in re.finditer(r"(?im)^#\s*(\w+):(.*)$", contents):
			vals[match.group(1).strip().lower()] = match.group(2).strip()
			
		if vals.has_key("exercise"):
			exercise = "<a href='view?chap="+chapter.lower().strip("chapter ")+"&exercise="+file.strip("exercise.py")+"'>"+vals["exercise"]+"</a>"
		else:
			exercise = "Unknown"
		
		if vals.has_key("start") & vals.has_key("end"): 
			timestring = "%I:%M:%S %p %m/%d/%Y"
			dur = duration(time.mktime(time.strptime(vals["end"], timestring))- time.mktime(time.strptime(vals["start"], timestring)));
		else:
			dur = "Unknown"
		
		if vals.has_key("rating"):	
			if vals['rating'] == "1":
				ratingcolor = "#FF687C"
			elif vals['rating'] == "2":
				ratingcolor = "#FF8C33"
			elif vals['rating'] == "3":
				ratingcolor = "#FFF04D"
			elif vals['rating'] == "4":
				ratingcolor = "#B2FF3E"
			rating = vals['rating']
		else:
			ratingcolor = "#FFFFFF"
			rating = "Unknown"

		if vals.has_key("note"):
			note = vals['note']
		else:
			note = "Unknown"

		exercises.append({"exercise":exercise, "duration":dur, "rating":rating, "ratingcolor":ratingcolor, "note":note})
	
	t2 = psp.PSP(req, filename="templates/chaptergrid.tmpl", vars={"exercises":exercises})
	
	return t2

def view(req, chap='', exercise=''):
	title = "Viewing Chapter "+ chap + ", Exercise " + str(int(exercise))
	content = ""
	if chap.count(".") != 0:
		title = "ERROR!"
		content = "You cannot use periods in the arguments!"
		return
	if exercise.count(".") != 0:
		title = "ERROR!"
		content = "You cannot use periods in the arguments!"
		return
		
	fullpath = "/var/www/html"
	relativepath = "/python/files/Chapter Exercises/Chapter " + chap + "/exercise" + exercise + ".py"
	path = fullpath + relativepath
	
	if os.path.isfile(path):
		curfile = open(path)
		code = curfile.read()
		formatter = HtmlFormatter()
		content = highlight(code, PythonLexer(), formatter)
		content = "<div style='overflow:auto; font-size:10pt;'>" + content + "</div><a href='"+relativepath+"'>View exercise"+exercise+".py</a>"
	else:
		title = "ERROR!"
		content = "Error! Invalid File"
	
	displayPage(req, [contentBlock(title,  content)], title, generateSideBarContent(), True)

	return
	
def SyntaxStyleSheet(req):
	#Displays the css data for Pygments' syntax highlighting
	req.content_type = "text/css"
	req.write(HtmlFormatter().get_style_defs('.highlight'))	
	return

def CurTimestamp(req):
	req.content_type = "text/html"
	req.write(time.strftime("%I:%M:%S %p %m/%d/%Y", time.localtime()))
	return
def newTemplate(req, chap="0", exer="0"):
	req.content_type = "text/html"
	if (chap.find(".") != -1 or exer.find(".") != -1):
		req.write("No hacking")
		return
	ret = "\r\n"
	chapter = str(int(chap))
	exercise = str(int(exer))
	templatestring = "# Chapter:\t\t"+chapter+ret
	templatestring = templatestring + "# Exercise:\t\t"+exercise+ret
	templatestring = templatestring + "# Start:\t\t"+time.strftime("%I:%M:%S %p %m/%d/%Y", time.localtime())+ret
	templatestring = templatestring + "# End:\t\t\t___________"+ret
	templatestring = templatestring + "# Rating:\t\t___________"+ret
	templatestring = templatestring + "# Note:\t\t\t___________"+ret
	templatestring = templatestring + ret
	
	
	filedir = "/var/www/html/python/files/Chapter Exercises/Chapter "+chapter+"/"
	filename = "exercise"+exercise.zfill(2)+".py"
	fullpath = filedir+filename
	
	if (not os.path.isdir(filedir)):
		req.write("Invalid File Path")
		return
	
	if (os.path.exists(fullpath)):
		req.write("File already exists for Chapter "+chapter+", Exercise "+exercise)		
	else:
		f = open(fullpath, "w")
		f.write(templatestring)
		f.close()
		req.write("Template for Chapter "+chapter+", Exercise "+exercise+" Created")
	return 
	
	
def BookExercises(req):
	bookprogramspath = "/var/www/html/python/files/Book Programs/"
	webpath = "/python/files/Book Programs/"
	contentblocks = []
	for dir in getBookPrograms():
		files = getfiles(bookprogramspath + dir)
		prettychaptername = "Chapter " + dir.strip("chapter")
		chapternum = int(dir.strip("chapter"))
		outstr = ""
		for file in files:
			outstr = outstr + ("<a href=\""+webpath + dir + "/" + file + "\">"+file+"</a><br />")
		contentblocks.insert(chapternum, (contentBlock(prettychaptername, outstr)))
	displayPage(req, contentblocks)
	
	return
