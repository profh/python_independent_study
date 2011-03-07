# Chapter:		0
# Exercise:		1
# Start:		01:11:43 PM 06/18/2007
# End:			01:12:43 PM 06/18/2007
# Rating:		4
# Note:			The Paint Program

from Tkinter import *
from PIL import Image, ImageTk

class StatusBar(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
		self.label.pack(fill=X)
	def set(self, format, *args):
		self.label.config(text=format % args)
		self.label.update_idletasks()
	def clear(self):
		self.label.config(text="")
		self.label.update_idletasks()

class PaintApp:
		
	def __init__(self, master):
		self.appwidth=900
		self.appheight=600
		self.currenttool = "cursor"
		self.master = master
		self.master.title("Paint Application")
		self.frame = Frame(self.master, width=self.appwidth, height=self.appheight, bg="", colormap="new")
		self.frame.grid()
		
		self.init_menubar()
		
		self.init_toolbar()
		self.init_drawingtools()
		self.init_colorpalette()
		self.init_canvas()
		self.init_statusbar()
		
		
		
	def init_canvas(self):
		self.canvas = Canvas(self.master, width=self.appwidth, height=self.appheight, bg="white")
		self.canvas.grid(row=1, column=0, columnspan=2)
	
	def newIcon(self, name):
		return PhotoImage(file="icons/"+name+".gif", width=32, height=32)
		
	def init_menubar(self):
		self.menu = Menu(self.master)
		self.master.config(menu=self.menu)
		
		filemenu = Menu(self.menu)
		self.menu.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="New", command=self.callback)
		filemenu.add_command(label="Open...", command=self.callback)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.frame.quit)

		helpmenu = Menu(self.menu)
		self.menu.add_cascade(label="Help", menu=helpmenu)
		helpmenu.add_command(label="About...", command=self.callback)
		
	def say_hi(self):
		print "Hi"
	
	def rgb2hex(self, rgb_tuple):
		hexcolor = "#%02x%02x%02x" % rgb_tuple
		# "%02x" == zero-padded, 2-digit hex values
		return hexcolor
	
	def setCurrentTool(self, tool):
		if (tool == self.currenttool):
			return
		self.currenttool = tool
		self.cursorbutton.config(relief=RAISED)
		self.linebutton.config(relief=RAISED)
		self.ellipsebutton.config(relief=RAISED)
		self.rectanglebutton.config(relief=RAISED)
		self.arcbutton.config(relief=RAISED)
		self.polygonbutton.config(relief=RAISED)
		self.status.set("You Selected the %s tool", tool)
		if tool == "cursor":
			self.cursorbutton.config(relief=SUNKEN)
		elif tool == "line":
			self.linebutton.config(relief=SUNKEN)
		elif tool == "ellipse":
			self.ellipsebutton.config(relief=SUNKEN)
		elif tool == "rectangle":
			self.rectanglebutton.config(relief=SUNKEN)
		elif tool == "arc":
			self.arcbutton.config(relief=SUNKEN)
		elif tool == "polygon":
			self.polygonbutton.config(relief=SUNKEN)
		return
	
	def callback(self):
		print "Callback"
	def pick_color(self, e):
		xpos = e.x
		ypos = e.y
		try:
			color = self.colorswatchimage.getpixel((xpos, ypos))
		except IndexError:
			statusstring = "Selection invalid. Defaulting to black"
			color = (0,0,0)
		else:	
			statusstring = "Color set to: " + str(color)
		self.status.set("%s", statusstring)
		
		self.currentcolor.config(background=self.rgb2hex(color))
		
	def event_lambda(f, *args, **kwds):
		return lambda event, f=f, args=args, kwds=kwds : f(*args, **kwds)
		
	def init_colorpalette(self):
		self.colorpalette = Frame(self.frame)
		
		self.currentcolor = Button(self.colorpalette, width=3, height=3, state=DISABLED, bg="black")
		self.currentcolor.pack(side=LEFT)
		
		self.colorpicker = Canvas(self.colorpalette, width=350, height=50, cursor="crosshair")
		self.colorswatchimage = Image.open("icons/colorstrip.png")
		self.colorswatch = ImageTk.PhotoImage(self.colorswatchimage)
		
		self.colorpicker.bind("<Button-1>",
			lambda
			event : self.pick_color(event)
			)
		
		self.colorpicker.create_image(0,0,image=self.colorswatch, anchor=W)
		
		self.colorpicker.pack(side=LEFT, fill=BOTH)
		
		self.colorpalette.grid(row=0, column=2)
		
	
	def init_drawingtools(self):
		self.drawingtools= Frame(self.frame, bg="red")

		cursoricon = self.newIcon("cursor")
		self.cursorbutton = Button(self.drawingtools, text="Cursor", width=34, height=34, relief=SUNKEN, command=lambda : self.setCurrentTool("cursor"), image=cursoricon)
		self.cursorbutton.bind("<Enter>", lambda e: self.status.set("%s", "Cursor"))
		self.cursorbutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.cursorbutton.grid(row=0,column=0)
		self.cursorbutton.image=cursoricon
		
		lineicon = self.newIcon("line")
		self.linebutton = Button(self.drawingtools, text="Line", width=34, height=34,command=lambda: self.setCurrentTool("line"), image=lineicon)
		self.linebutton.bind("<Enter>", lambda e: self.status.set("%s", "Draws a line from one point to another"))
		self.linebutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.linebutton.grid(row=0,column=1)
		self.linebutton.image=lineicon

		ellipseicon = self.newIcon("ellipse")
		self.ellipsebutton = Button(self.drawingtools, text="ellipse", width=34, height=34, command=lambda : self.setCurrentTool("ellipse"), image=ellipseicon)
		self.ellipsebutton.bind("<Enter>", lambda e: self.status.set("%s", "Draws an ellipse within a given boundary"))
		self.ellipsebutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.ellipsebutton.grid(row=0,column=2)
		self.ellipsebutton.image=ellipseicon

		rectangleicon = self.newIcon("rectangle")
		self.rectanglebutton = Button(self.drawingtools, text="rectangle", width=34, height=34, command=lambda : self.setCurrentTool("rectangle"), image=rectangleicon)
		self.rectanglebutton.bind("<Enter>", lambda e: self.status.set("%s", "Draws an rectangle within a given boundary"))
		self.rectanglebutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.rectanglebutton.grid(row=0,column=3)
		self.rectanglebutton.image=rectangleicon

		arcicon = self.newIcon("arc")
		self.arcbutton = Button(self.drawingtools, text="arc", width=34, height=34, command=lambda : self.setCurrentTool("arc"), image=arcicon)
		self.arcbutton.bind("<Enter>", lambda e: self.status.set("%s", "Draws an arc within a given boundary"))
		self.arcbutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.arcbutton.grid(row=0,column=4)
		self.arcbutton.image=arcicon

		polygonicon = self.newIcon("polygon")
		self.polygonbutton = Button(self.drawingtools, text="polygon", width=34, height=34, command=lambda : self.setCurrentTool("polygon"), image=polygonicon)
		self.polygonbutton.bind("<Enter>", lambda e: self.status.set("%s", "Draws an polygon . Once you are finished clicking the points, click the polygon button again to complete the shape"))
		self.polygonbutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.polygonbutton.grid(row=0,column=5)
		self.polygonbutton.image=polygonicon
		
		self.drawingtools.grid(row=0, column=1, sticky=W)
		

	def init_toolbar(self):
		self.toolbar = Frame(self.frame)
		newicon = self.newIcon("new")
		self.newbutton = Button(self.toolbar, text="New", width=34, height=34, command=self.callback, image=newicon)
		self.newbutton.bind("<Enter>", lambda e: self.status.set("%s", "Creates a New Document"))
		self.newbutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.newbutton.grid(row=0,column=0, sticky=W)
		self.newbutton.image=newicon
		
		openicon = self.newIcon("open")
		self.openbutton = Button(self.toolbar, text="Open", width=34, height=34, command=self.callback, image=openicon)
		self.openbutton.bind("<Enter>", lambda e: self.status.set("%s", "Opens a file"))
		self.openbutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.openbutton.grid(row=0,column=1, sticky=W)
		self.openbutton.image = openicon
				
		saveicon = self.newIcon("save")
		self.savebutton = Button(self.toolbar, text="Save", width=34, height=34, command=self.callback, image=saveicon)
		self.savebutton.bind("<Enter>", lambda e: self.status.set("%s", "Saves the current document"))
		self.savebutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.savebutton.grid(row=0,column=2,sticky=W)
		self.savebutton.image = saveicon #save image from garbage collection
		
		undoicon = self.newIcon("undo")
		self.undobutton = Button(self.toolbar, text="Undo", width=34, height=34, command=self.callback, state=DISABLED, image=undoicon)
		self.undobutton.bind("<Enter>", lambda e: self.status.set("%s", "Undo: undoes the most recent command"))
		self.undobutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.undobutton.grid(row=0,column=3, sticky=W)
		self.undobutton.image = undoicon

		eraseicon = self.newIcon("erase")
		self.erasebutton = Button(self.toolbar, text="Erase", width=34, height=34, command=self.callback, image=eraseicon)
		self.erasebutton.bind("<Enter>", lambda e: self.status.set("%s", "Clears out existing drawing"))
		self.erasebutton.bind("<Leave>", lambda e: self.status.set("%s", ""))
		self.erasebutton.grid(row=0,column=4, sticky=W)
		self.erasebutton.image = eraseicon

		self.toolbar.grid(row=0, column=0, sticky=W, padx=10)
		
	def init_statusbar(self, defaultformat="%s", defaultmessage="Paint Application Initalized"):
		self.status = StatusBar(self.master)
		self.status.grid(row=2, column=0, columnspan=3)
		self.status.set(defaultformat,defaultmessage)


root = Tk()
app = PaintApp(root)
root.mainloop()


