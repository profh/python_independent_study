# Components_4.py for chapter 10 examples

from Tkinter   import *
from GUICommon import *
from Common    import *

st_wid = []
ops = ['turnon','turnoff','warn','alarm','blinkon','blinkoff']

glb = DummyClass()

class LED(GUICommon): 
    def __init__(self, master=None, width=25, height=25, 
                 appearance=FLAT,
                 status=STATUS_ON, bd=1, 
                 bg=None, 
                 shape=SQUARE, outline="",
                 blink=0, blinkrate=1,
                 orient=POINT_UP,
                 takefocus=0):
        # preserve attributes
        self.master       = master
        self.shape        = shape
        self.Colors       = [None, Color.OFF, Color.ON,
                             Color.WARN, Color.ALARM, '#00ffdd']
        self.status       = status
        self.blink        = blink
        self.blinkrate    = int(blinkrate)
        self.on           = 0
        self.onState      = None

        st_wid.append(self)    # register for animation
        
        if not bg:
            bg = Color.PANEL

        ## Base frame to contain light
        self.led_frame=Frame(master, relief=appearance, bg=bg, bd=bd, 
                             takefocus=takefocus)

        basesize = width
        d = center = int(basesize/2)

        if self.shape == SQUARE:
            self.canvas=Canvas(self.led_frame, height=height, width=width, 
                               bg=bg, bd=0, highlightthickness=0)

            self.light=self.canvas.create_rectangle(0, 0, width, height,
                                                    fill=Color.ON)
        elif self.shape == ROUND:
            r = int((basesize-2)/2)
            self.canvas=Canvas(self.led_frame, width=width, height=width, 
                               highlightthickness=0, bg=bg, bd=0)
            if bd > 0:
                self.border=self.canvas.create_oval(center-r, center-r, 
                                                    center+r, center+r)
                r = r - bd
            self.light=self.canvas.create_oval(center-r-1, center-r-1, 
                                               center+r, center+r, 
                                               fill=Color.ON,
                                               outline=outline)
        else:  # Default is an ARROW
            self.canvas=Canvas(self.led_frame, width=width, height=width, 
                               highlightthickness=0, bg=bg, bd=0)
            x = d
            y = d
            VL = ARROW_HEAD_VERTICES[orient] 
            self.light=self.canvas.create_polygon(eval(VL[0]),
                              eval(VL[1]), eval(VL[2]), eval(VL[3]),
                              eval(VL[4]), eval(VL[5]), eval(VL[6]),
                              eval(VL[7]), outline = outline)

        self.canvas.pack(side=TOP, fill=X, expand=NO)
        self.update()

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState     # Current ON color
                self.on = 1

        # Set color for current status
        self.canvas.itemconfig(self.light, fill=self.Colors[self.status])

        self.canvas.update_idletasks()

        if self.blink:
            self.led_frame.after(self.blinkrate * 1000, self.update)

class CLED(GUICommon): 
    def __init__(self, frame=None, ocanv=None, width=25, height=25, 
                 status=STATUS_ON, bd=0, 
                 bg=None, 
                 shape=SQUARE, outline="",
                 blink=0, blinkrate=1,
                 orient=POINT_UP,
                 takefocus=0,
                 relx=0, rely=0):
        # preserve attributes
        self.frame        = frame
        self.ocanv        = ocanv
        self.shape        = shape
        self.Colors       = [None, Color.OFF, Color.ON,
                             Color.WARN, Color.ALARM, '#00ffdd']
        self.status       = status
        self.blink        = blink
        self.blinkrate    = int(blinkrate)
        self.on           = 0
        self.onState      = None

        st_wid.append(self)    # register for animation
        
        basesize = width
        d = center = int(basesize/2)

        if self.shape == SQUARE:
            self.light=self.ocanv.create_rectangle(relx, rely,
                                                   relx+width, rely+height,
                                                    fill=Color.ON)
        else: # Default is an round
            r = int((basesize-2)/2)
            if bd > 0:
                self.border=self.ocanv.create_oval(relx-r, rely-r, 
                                                    rely+r, rely+r)
                r = r - bd
            self.light=self.ocanv.create_oval(relx-r-1, rely-r-1, 
                                               relx+r, rely+r, 
                                               fill=Color.ON,
                                               outline=outline)
        self.update()

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState     # Current ON color
                self.on = 1

        # Set color for current status
        self.ocanv.itemconfig(self.light, fill=self.Colors[self.status])

        self.frame.update_idletasks()

        if self.blink:
            self.frame.after(self.blinkrate * 1000, self.update)

class Screen(GUICommon):
     def __init__(self, master, bg=Color.PANEL, height=1, width=1):
         self.screen_frame = Frame(master, width=width, height=height,
                                   bg=bg, bd=0)
         self.base = bg
         self.set_colors(self.screen_frame)
         radius = 4         # radius of an air hole
         ssize  = radius*3  # spacing between holes
         
         rows = int(height/ssize)
         cols = int(width/ssize)
                
         self.canvas = Canvas(self.screen_frame, height=height, width=width, 
                               bg=bg, bd=0, highlightthickness=0)

         self.canvas.pack(side=TOP, fill=BOTH, expand=NO)

         y = ssize - radius
         for r in range(rows):
             x0 = ssize -radius
             for c in range(cols):
                 x = x0 + (ssize*c)
                 self.canvas.create_oval(x-radius, y-radius,
                                         x+radius, y+radius,
                                         fill=self.dbase,
                                         outline=self.lbase)
             y = y + ssize

class PowerConnector:
    def __init__(self, master, bg=Color.PANEL):
        self.socket_frame = Frame(master, relief="raised", width=60,
	                  height=40,  bg=bg, bd=4)
	inside=Frame(self.socket_frame, relief="sunken", width=56,
                     height=36, bg=Color.INSIDE, bd=2)
	inside.place(relx=.5, rely=.5, anchor=CENTER)
	ground=Frame(inside, relief="raised", width=6, height=10,
		          bg=Color.CHROME, bd=2)
	ground.place(relx=.5, rely=.3, anchor=CENTER)
	p1=Frame(inside, relief="raised", width=6, height=10,
		          bg=Color.CHROME, bd=2)
	p1.place(relx=.25, rely=.7, anchor=CENTER)
	p2=Frame(inside, relief="raised", width=6, height=10,
		          bg=Color.CHROME, bd=2)
	p2.place(relx=.75, rely=.7, anchor=CENTER)

class PowerSwitch(GUICommon):
    def __init__(self, master, label='I   0', base=Color.PANEL):
        self.base = base
        self.set_colors(master)
        self.switch_frame = Frame(master, relief="raised", width=45,
	                  height=28, bg=self.vlbase, bd=4)
	switch = Frame(self.switch_frame, relief="sunken", width=32,
                       height=22, bg=self.base, bd=2)
	switch.place(relx=0.5, rely=0.5, anchor=CENTER)
	lbl=Label(switch, text=label, font=("Verdana", 10, "bold"), 
		       fg='white', bd=0, bg=self.dbase)
	lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

class Enet10baseT(GUICommon):
    def __init__(self, master, orient=HW_UP, status=STATUS_ON,
                 port=-1, fid='', xwidth=30, xheight=24):
	self.hitID  = fid
        self.Colors       = [None, Color.CHROME, Color.ON,
                             Color.WARN, Color.ALARM, '#00ffdd']
        if orient == HW_UP or orient == HW_DOWN:
            width   = xwidth
            height  = xheight
            iwidth  = width*0.8
            iheight = height - (width*0.2)
            jwidth  = width / 3
            jheight = height / 4
        else:
            width   = xheight
            height  = xwidth
            iwidth  = width - (height*0.2)
            iheight = height*0.8
            jwidth  = height / 3
            jheight = width / 4
            
        self.status = status
        self.blink        = 0
        self.blinkrate    = 1
        self.on           = 0
        self.onState      = None
        self.high         = FALSE

        st_wid.append(self)    # register for animation

        self.j45_frame = Frame(master, width=width, height=height, bd=2, 
                               relief="raised", bg=Color.CHROME,
                               takefocus=1)
	self.j45_frame.pack(fill=BOTH, expand=1)
	self.j45_frame.bind('<FocusIn>', self.focus_in)
	self.j45_frame.bind('<FocusOut>', self.focus_out)
	self.i1 = Frame(self.j45_frame, relief="sunken", width=iwidth,
                        height=iheight, bg=Color.INSIDE, bd=1)
	self.i1.place(relx=0.05, rely=0.04, anchor=NW)
	self.i2 = Frame(self.j45_frame, relief="flat", width=jwidth,
                        height=jheight, bg=Color.INSIDE, bd=2)

        xx, yy = [(0.5,0),(0.5,1),(0,0.5),(1,0.5)][orient]
        self.i2.place(relx=xx, rely=yy, anchor=CENTER)

	if self.hitID:
	    self.hitID = '%s.%d' % (self.hitID, port)
	    for widget in [self.j45_frame, self.i1, self.i2]:
	        widget.bind('<KeyPress-space>', self.panelMenu)
	        widget.bind('<Button-1>', self.panelMenu)

    def focus_in(self, event):
	self.last_background = self.j45_frame['background']
	self.j45_frame['background'] = Color.HIGHLIGHT
        self.high = TRUE
	self.update()

    def focus_out(self, event):
	self.j45_frame['background'] = self.last_background
        self.high = FALSE
	self.update()

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState  # Current ON color
                self.on = 1

        # Set color for current status
        if not self.high:
            self.j45_frame['background'] = self.Colors[self.status]

        self.j45_frame.update_idletasks()

        if self.blink:
            self.j45_frame.after(self.blinkrate * 1000, self.update)

class BNC(GUICommon):
    def __init__(self, master, status=0, diameter=18, port=-1, fid=''): 
        self.base = master['background']
	self.hitID = fid
	self.status=status
        self.blink        = 0
        self.blinkrate    = 1
        self.on           = 0
        self.onState      = None
        self.Colors       = [None, Color.CHROME, Color.ON,
                             Color.WARN, Color.ALARM, '#00ffdd']

        st_wid.append(self)    # register for animation

	basesize = diameter+6
        self.bnc_frame = Frame(master, relief="flat", bg=self.base,
                               bd=0, highlightthickness=0, takefocus=1)
	self.bnc_frame.pack(expand=0)
	self.bnc_frame.bind('<FocusIn>', self.focus_in)
	self.bnc_frame.bind('<FocusOut>', self.focus_out)
	self.canvas=Canvas(self.bnc_frame, width=basesize, height=basesize,
                           highlightthickness=0, bg=self.base, bd=0)
	center = basesize/2
	r = diameter/2

	self.pins=self.canvas.create_rectangle(0, center+2, basesize-1, 10,
                                               fill=Color.CHROME)
	self.bnc=self.canvas.create_oval(center-r, center-r,
                                         center+r, center+r, 
                                         fill=Color.CHROME, outline="black")
	r = r-3
	self.canvas.create_oval(center-r, center-r, center+r, center+r, 
                                fill=Color.INSIDE, outline='black')
	r = r-2
	self.canvas.create_oval(center-r, center-r, center+r, center+r, 
                                fill=Color.CHROME)
	r = r-3
	self.canvas.create_oval(center-r, center-r, center+r, center+r, 
                                fill=Color.INSIDE, outline='black')

	self.canvas.pack(side=TOP, fill=X, expand=0)

	if self.hitID:
	    self.hitID = '%s.%d' % (self.hitID, port)
	    for widget in [self.bnc_frame]:
	        widget.bind('<KeyPress-space>', self.panelMenu)
	        widget.bind('<Button-1>', self.panelMenu)
	    for widget in [self.canvas]:
	        widget.bind('<1>', self.panelMenu)

    def focus_in(self, event):
	self.last_background = self.canvas.itemcget(self.bnc, 'fill')
        self.canvas.itemconfig(self.bnc, fill=Color.HIGHLIGHT)
	self.update()

    def focus_out(self, event):
        self.canvas.itemconfig(self.bnc, fill=self.last_background)
	self.update()

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState     # Current ON color
                self.on = 1

	# now update the status
        self.canvas.itemconfig(self.bnc,  fill=self.Colors[self.status])
        self.canvas.itemconfig(self.pins, fill=self.Colors[self.status])

	self.bnc_frame.update_idletasks()

        if self.blink:
            self.bnc_frame.after(self.blinkrate * 1000, self.update)

class FDDI(GUICommon):
    def __init__(self, master, status=STATUS_OFF, orient=HW_HORIZONTAL,
                 port=-1, fid=''):
	self.hitID        = fid
        self.status       = status
        self.blink        = 0
        self.blinkrate    = 1
        self.on           = 0
        self.onState      = None
        self.high         = FALSE
        self.Colors       = [None, Color.DISP, Color.ON,
                             Color.WARN, Color.ALARM, '#00ffdd']
        
        if orient == HW_HORIZONTAL:
            width   = 46
            height  = 20
            iwidth  = 16
            iheight = 15
            ix = 0
        else:
            width   = 20
            height  = 46
            iwidth  = 15
            iheight = 16
            ix = 1
            
        st_wid.append(self)    # register for animation

        self.fddi_frame = Frame(master, relief="raised", width=width,
                                height=height, bg=Color.DISP, bd=1,
                                takefocus=1)
	self.fddi_frame.bind('<FocusIn>', self.focus_in)
	self.fddi_frame.bind('<FocusOut>', self.focus_out)
	self.rx = Frame(self.fddi_frame, relief="sunken", width=iwidth,
                        height=iheight, bg=Color.INSIDE, bd=1)
	self.rx.place(relx=[0.05,0.06][ix], rely=0.05, anchor=NW)
	self.tx = Frame(self.fddi_frame, relief="sunken", width=iwidth,
                        height=iheight, bg=Color.INSIDE, bd=1)
	self.tx.place(relx=0.95, rely=[0.05,0.95][ix], anchor=[NE,SE][ix])
	if self.hitID:
	    self.hitID = '%s.%d' % (self.hitID, port)
	    for widget in [self.fddi_frame, self.rx, self.tx]:
	        widget.bind('<KeyPress-space>', self.panelMenu)
	        widget.bind('<Button-1>', self.panelMenu)

    def focus_in(self, event):
	self.last_background = self.fddi_frame['background']
	self.fddi_frame['background'] = Color.HIGHLIGHT
        self.high = TRUE
	self.update()

    def focus_out(self, event):
	self.fddi_frame['background'] = self.last_background
        self.high = FALSE

	self.update()

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState  # Current ON color
                self.on = 1

        # Set color for current status
        if not self.high:
            self.fddi_frame['background'] = self.Colors[self.status]

        self.fddi_frame.update_idletasks()

        if self.blink:
            self.fddi_frame.after(self.blinkrate * 1000, self.update)

class JConnector(GUICommon):
    def __init__(self, master, width, height, orient=HW_HORIZONTAL, 
		 port=-1, fid='', status=STATUS_OFF): 
	self.hitID        = fid
        self.status       = status
        self.blink        = 0
        self.blinkrate    = 1
        self.on           = 0
        self.onState      = None
	if orient == HW_HORIZONTAL:
	    use_width  = width
	    use_height = height
	else:
	    use_width  = height
	    use_height = width

        st_wid.append(self)    # register for animation

        self.j_frame = Frame(master, relief="raised", width=use_width,
                             height=use_height, bg=Color.CHROME, bd=2, 
                             takefocus=1)
	self.j_frame.bind('<FocusIn>', self.focus_in)
	self.j_frame.bind('<FocusOut>', self.focus_out)
        self.body = Frame(self.j_frame, relief="sunken", width=use_width-6,
	                  height=use_height-6, bg=Color.CHROME, bd=2)
	self.body.place(relx=0.5, rely=0.5, anchor=CENTER)
	self.i1 = Frame(self.body, relief="sunken", width=use_width-8, 
			height=use_height-8,
	                bg=Color.INSIDE, bd=1)
	self.i1.place(relx=0.5, rely=0.5, anchor=CENTER)
	if self.hitID:
	    self.hitID = '%s.%d' % (self.hitID, port)
	    for widget in [self.j_frame, self.body, self.i1]:
	        widget.bind('<KeyPress-space>', self.panelMenu)
	        widget.bind('<Button-1>', self.panelMenu)

    def update(self):
        # First do the blink, if set to blink
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status
                self.status  = STATUS_OFF
                self.on      = 0                            
            else:
                if self.onState:
                    self.status = self.onState  # Current ON color
                self.on = 1

	self.j_frame.update_idletasks()

        if self.blink:
            self.j_frame.after(self.blinkrate * 1000, self.update)

    def turnon(self):
	self.j_frame['background'] = Color.ON
	self.body['background'] = Color.CHROME
	self.update()

    def turnoff(self):
	self.j_frame['background'] = Color.CHROME
	self.body['background'] = Color.CHROME
	self.update()

    def warn(self):
	self.j_frame['background'] = Color.WARN
	self.body['background'] = Color.WARN
	self.update()

    def alarm(self):
	self.j_frame['background'] = Color.ALARM
	self.body['background'] = Color.ALARM
	self.update()

    def focus_in(self, event):
	self.last_j_frame_background = self.j_frame['background']
	self.last_body_background = self.body['background']
	self.j_frame['background'] = Color.HIGHLIGHT
	self.body['background'] = Color.HIGHLIGHT
	self.update()

    def focus_out(self, event):
	self.j_frame['background'] = self.last_j_frame_background
	self.body['background'] = self.last_body_background
	self.update()

class J9(JConnector):
    def __init__(self, master, port=-1, fid='', orient=HW_HORIZONTAL,
                 status=STATUS_OFF):
	JConnector.__init__(self, master=master, width=40, height=22, 
			    port=port, fid=fid,
			    status=status, orient=orient)

class J25(JConnector):
    def __init__(self, master, port=-1, fid='', orient=HW_HORIZONTAL,
                 status=STATUS_OFF):
	JConnector.__init__(self, master=master, width=100, height=22, 
			    port=port, fid=fid,
			    status=status, orient=orient)

class J50(JConnector):
    def __init__(self, master, port=-1, fid='', orient=HW_HORIZONTAL,
                 status=STATUS_OFF):
	JConnector.__init__(self, master=master, width=90, height=18, 
			    port=port, fid=fid,
			    status=status, orient=orient)

class FastSerial(JConnector):
    def __init__(self, master, port=-1, fid='', orient=HW_HORIZONTAL,
                 status=STATUS_OFF):
	JConnector.__init__(self, master=master, width=66, height=24, 
			    port=port, fid=fid,
			    status=status, orient=orient)

class PanelText:
    def __init__(self, master=None, appearance="flat", width=0, 
		 bg='gray15', bd=0, text="", fg='yellow'):
	# preserve various values

        self.text_frame = Frame(master, relief=appearance, bg=bg, bd=bd,
                                highlightthickness=0, takefocus=0)

#        font = ("PixelPoint", 10)
        font = ("Verdana", 10)
        self.text=Label(self.text_frame, text=text[:2], fg=fg,
                        bg=bg, font=font)
	self.text.pack()

    def display(self, newtext):
	self.text['text'] = newtext
	self.update()

class PowerSupply(GUICommon):
    def __init__(self, master, width=160, height=130, bg=Color.PANEL,
                 status=STATUS_ON): 
        self.base = bg
        self.set_colors(master)
        
        self.psu_frame = Frame(master, relief=SUNKEN, bg=self.dbase, bd=2, 
                               width=width, height=height)

	Label(self.psu_frame, text='DC OK', fg='white',
              bg=self.dbase, font=('Verdana', 10, 'bold'),
              bd=0).place(relx=.8, rely=.15, anchor=CENTER)
	self.led = LED(self.psu_frame, height=12, width=12, shape=ROUND,
                       bg=self.dbase)
	self.led.led_frame.place(relx=0.8, rely=0.31, anchor=CENTER)
	lsub = Frame(self.psu_frame, width=width/1.2, height=height/2,
                     bg=self.dbase, bd=1, relief=GROOVE)
	lsub.place(relx=0.5, rely=0.68, anchor=CENTER)
	pwr=PowerConnector(lsub)
	pwr.socket_frame.place(relx=0.30, rely=0.5, anchor=CENTER)
	sw=PowerSwitch(lsub)
	sw.switch_frame.place(relx=0.75, rely=0.5, anchor=CENTER)
    
class Screw(GUICommon):
    def __init__(self, master, diameter=18, base="gray40", bg=Color.PANEL):
        self.base = base

	basesize = diameter+6
        self.screw_frame = Frame(master, relief="flat", bg=bg, bd=0, 
			  highlightthickness=0)
        self.set_colors(self.screw_frame)

	canvas=Canvas(self.screw_frame, width=basesize, height=basesize,
                      highlightthickness=0, bg=bg, bd=0)
	center = basesize/2
	r = diameter/2
        r2 = r - 4.0

	canvas.create_oval(center-r, center-r, center+r, center+r, 
                           fill=self.base, outline=self.lbase)
	canvas.create_rectangle(center-r2, center-0.2,
                                center+r2, center+0.2,
                                fill=self.dbase, width=0)
	canvas.create_rectangle(center-0.2, center-r2,
                                center+0.2, center+r2,
                                fill=self.dbase, width=0)
	canvas.pack(side="top", fill='x', expand='no')

class StandardLEDs(GUICommon):
    def __init__(self, master=None, bg=Color.CARD):
        for led, label, xpos, ypos, state in [('flt', 'Flt', 0.3, 0.88, 1),
                                              ('pwr', 'Pwr', 0.7, 0.88, 2)]:
            setattr(self, led, LED(self.card_frame,shape=ROUND,width=8,
                                          status=state, bg=bg))
            getattr(self, led).led_frame.place(relx=xpos, rely=ypos,
                                                      anchor=CENTER)
            Label(self.card_frame, text=label,
                  font=("verdana", 4), fg="white",
                  bg=bg).place(relx=xpos,rely=(ypos+0.028), anchor=CENTER)
        
class CardBlank(GUICommon):
    def __init__(self, master=None, width=20, height=396,
		 appearance="raised", bd=2, base=Color.CARD):
        self.base = base
        self.set_colors(master)
	self.card_frame=Frame(master, relief=appearance, height=height, 
                              width=width, bg=base, bd=bd)
	top_pull = CardPuller(self.card_frame, CARD_TOP, width=width)
	top_pull.puller_frame.place(relx=.5, rely=0, anchor=N)
	bottom_pull = CardPuller(self.card_frame, CARD_BOTTOM, width=width)
	bottom_pull.puller_frame.place(relx=.5, rely=1.0, anchor=S)

class CardPuller(GUICommon):
    def __init__(self, master, torb, width=20):
        self.base = master['background']
        self.set_colors(master)
	self.puller_frame=Frame(master, width=width, height=32,
                                bg=self.lbase, relief='flat')
	Frame(self.puller_frame, width=width/8, height=8,
              bg=self.dbase).place(relx=1.0, rely=[1.0,0][torb],
                                   anchor=[SE,NE][torb])
	Frame(self.puller_frame, width=width/3, height=24,
              bg=self.vdbase).place(relx=1.0, rely=[0,1.0][torb],
                                    anchor=[NE,SE][torb])
        Screw(self.puller_frame, diameter=10, base=self.base,
              bg=self.lbase).screw_frame.place(relx=0.3, rely=[0.2,0.8][torb],
                                               anchor=CENTER)
        
class E10BASETCard(CardBlank,StandardLEDs):
    def __init__(self, master, width=1, height=1):
	CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        yy = 0.26
        for i in range(8):
            setattr(self, 'j%d' % (i+1), Enet10baseT(self.card_frame,
               fid="10Base-T-%d", port=i+1,orient=HW_LEFT, status=STATUS_OFF))
            getattr(self, 'j%d' % (i+1)).j45_frame.place(relx=0.5, rely=yy,
                                                       anchor=CENTER)
            yy = yy + 0.08

        xypos = [(0.2,0.1), (0.8,0.1),
                 (0.2,0.13),(0.8,0.13),
                 (0.2,0.16),(0.8,0.16),
                 (0.2,0.19),(0.8,0.19)]
        
        for i in range(8):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), LED(self.card_frame,shape=ROUND,
                        width=6, status=STATUS_ON, bg=bg))
            getattr(self, 'led%d' % (i+1)).led_frame.place(relx=xpos,
                                                  rely=ypos,anchor=CENTER)
        for lbl, ypos in [('1 2', 0.1), ('3 4', 0.13),
                          ('5 6', 0.16),('7 8', 0.19)]:
            Label(self.card_frame,text=lbl,
                  font=("verdana", 4), fg="white",
                  bg=bg).place(relx=0.5,rely=ypos,anchor=CENTER)
                 
class FastSerialCard(CardBlank,StandardLEDs):
    def __init__(self, master, width=1, height=1):
	CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        yy = 0.28
        for i in range(4):
            setattr(self, 'fs%d' % (i+1), J9(self.card_frame,
                        fid="FastSerial-%d", port=i+1, orient=HW_VERTICAL,
                        status=STATUS_OFF))
            getattr(self, 'fs%d' % (i+1)).j_frame.place(relx=0.5,
                                               rely=yy,anchor=CENTER)
            yy = yy + 0.167

        xypos = [(0.2,0.1), (0.8,0.1),
                 (0.2,0.13),(0.8,0.13),
                 (0.2,0.16),(0.8,0.16),
                 (0.2,0.19),(0.8,0.19)]
        
        for i in range(8):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), LED(self.card_frame,shape=ROUND,
                        width=6, status=STATUS_ON, bg=bg))
            getattr(self, 'led%d' % (i+1)).led_frame.place(relx=xpos,
                                                  rely=ypos,anchor=CENTER)
        for lbl, ypos in [('1', 0.1), ('2', 0.13),
                          ('3', 0.16),('4', 0.19)]:
            Label(self.card_frame,text=lbl,
                  font=("verdana", 4), fg="white",
                  bg=bg).place(relx=0.5,rely=ypos,anchor=CENTER)
                 
class ProcessorCard(CardBlank,StandardLEDs):
    def __init__(self, master, width=1, height=1):
	CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        self.j45=Enet10baseT(self.card_frame,fid="ClockPort",
                             port=1,orient=HW_LEFT, status=STATUS_OFF)
        self.j45.j45_frame.place(relx=0.5,rely=0.25,anchor=CENTER)
        lbl=Label(self.card_frame,text="Clock",
                  font=("verdana", 6), fg="white",bg=bg)
        lbl.place(relx=0.5, rely=0.20,anchor=S)

        self.cmd=J25(self.card_frame,fid="ControlPort",
                     port=1,orient=HW_VERTICAL, status=STATUS_OFF)
        self.cmd.j_frame.place(relx=0.5,rely=0.65,anchor=CENTER)
        Label(self.card_frame,text="CLI",
              font=("verdana", 6), fg="white",
              bg=bg).place(relx=0.5, rely=0.52,anchor=S)
                 
        xypos = [(0.3,0.35),(0.7,0.35),
                 (0.3,0.38),(0.7,0.38),
                 (0.3,0.41),(0.7,0.41),
                 (0.3,0.44),(0.7,0.44)]
        
        for i in range(8):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), LED(self.card_frame,shape=ROUND,
                        width=6, status=STATUS_ON, bg=bg))
            getattr(self, 'led%d' % (i+1)).led_frame.place(relx=xpos,
                                                  rely=ypos,anchor=CENTER)

class SwitchCard(CardBlank,StandardLEDs):
    def __init__(self, master, width=1, height=1):
	CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        xypos = [(0.3,0.35),(0.7,0.35),
                 (0.3,0.38),(0.7,0.38)]
        
        for i in range(4):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), LED(self.card_frame,shape=ROUND,
                        width=6, status=STATUS_ON, bg=bg))
            getattr(self, 'led%d' % (i+1)).led_frame.place(relx=xpos,
                                                  rely=ypos,anchor=CENTER)

        self.status = PanelText(self.card_frame, text='OK')
        self.status.text_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

class T3AccessCard(CardBlank,StandardLEDs):
    def __init__(self, master, width=1, height=1):
	CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        for port, lbl, tag, ypos in [(1,'RX1','T3AccessRX', 0.30),
                                     (2,'TX1','T3AccessTX', 0.40),
                                     (3,'RX2','T3AccessRX', 0.65),
                                     (4,'TX2','T3AccessRX', 0.75)]:
            setattr(self, 'bnc%d' % port, BNC(self.card_frame, fid=tag,
                                              port=port))
            getattr(self, 'bnc%d' % port).bnc_frame.place(relx=0.5,
                                              rely=ypos,anchor=CENTER)
            Label(self.card_frame,text=lbl,
                  font=("verdana", 6), fg="white",
                  bg=bg).place(relx=0.5, rely=(ypos+0.045), anchor=CENTER)
        for led, lbl, xpos, ypos, state in [('rxc','RXC',0.3,0.18,2),
                                            ('oos','OOS',0.7,0.18,1),
                                            ('flt','FLT',0.3,0.23,1),
                                            ('syn','SYN',0.7,0.23,2),
                                            ('rxc','RXC',0.3,0.53,2),
                                            ('oos','OOS',0.7,0.53,1),
                                            ('flt','FLT',0.3,0.58,1),
                                            ('syn','SYN',0.7,0.58,2)]:
            setattr(self, led, LED(self.card_frame,shape=ROUND,width=8,
                                   status=state, bg=bg))
            getattr(self, led).led_frame.place(relx=xpos,
                                        rely=ypos,anchor=CENTER)
            Label(self.card_frame,text=lbl,
                  font=("verdana", 4), fg="white",
                  bg=bg).place(relx=xpos, rely=(ypos+0.028), anchor=CENTER)
            
class OC3Card(CardBlank,StandardLEDs):
    def __init__(self, master, width=1, height=1):
	CardBlank.__init__(self, master=master, width=width, height=height)
        bg=master['background']
        StandardLEDs.__init__(self, master=master, bg=bg)
        yy = 0.28
        for i in range(4):
            setattr(self, 'oc3%d' % (i+1), FDDI(self.card_frame, fid="OC3-%d",
                 port=i+1, orient=HW_VERTICAL, status=STATUS_OFF))
            getattr(self, 'oc3%d' % (i+1)).fddi_frame.place(relx=0.5,
                                                  rely=yy, anchor=CENTER)
            yy = yy + 0.167

        left = TRUE
        yy =0.213
        for i in range(8):
            if left:
                xpos = 0.3
            else:
                xpos = 0.7
            setattr(self, 'led%d' % (i+1), LED(self.card_frame, shape=ROUND,
                              width=6, status=STATUS_ON, bg=bg))
            getattr(self, 'led%d' % (i+1)).led_frame.place(relx=xpos,
                                                  rely=yy, anchor=CENTER)
            if left:
                left = FALSE
            else:
                left = TRUE
                yy = yy + 0.167

class C6C110_CardBlank(GUICommon):
    def __init__(self, master=None, width=10, height=10,
		 appearance=FLAT, bd=0):
	self.card_frame=Frame(master, relief=appearance, height=height, 
                              width=width, bd=bd, highlightthickness=0)

class C6C110_FDDI(C6C110_CardBlank):
    def __init__(self, master, slot=0):
        self.img = PhotoImage(file='images/6c110_fddi.gif')
        setattr(glb,  'img%d' % slot, self.img)
        self.width  = self.img.width()
        self.height = self.img.height()

	C6C110_CardBlank.__init__(self, master=master, width=self.width,
                                  height=self.height)
        xypos = [(9,43),(13,70),(18,70),
                 (13,105),(18,105),
                 (13,140),(18,140),
                 (13,175),(18,175),
                 (13,203),(18,203),
                 (13,238),(18,238),
                 (13,273),(18,273),
                 (12,308),(17,308) ]
        
        self.canvas = Canvas(self.card_frame, width=self.width,
                             bd=0,highlightthickness=0,
                             height=self.height,selectborderwidth=0)
        self.canvas.pack(side="top", fill=BOTH, expand='no')
        self.canvas.create_image(0,0,anchor=NW,
                                 image=eval('glb.img%d' % slot))

        for i in range(len(xypos)):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), CLED(self.card_frame,
                          self.canvas, shape=ROUND, width=4, status=STATUS_ON,
                          relx=xpos, rely=ypos))

class C6C110_ENET(C6C110_CardBlank):
    def __init__(self, master, slot=0):
        self.img = PhotoImage(file='images/6c110_enet.gif')
        setattr(glb,  'img%d' % slot, self.img)
        self.width  = self.img.width()
        self.height = self.img.height()

	C6C110_CardBlank.__init__(self, master=master, width=self.width,
                                  height=self.height)
        xypos = [(10,180),(10,187),
                 (10,195),(10,203),(10,210),(10,235),
                 (10,242)]
        
        self.canvas = Canvas(self.card_frame, width=self.width,
                             bd=0,highlightthickness=0,
                             height=self.height,selectborderwidth=0)
        self.canvas.pack(side="top", fill=BOTH, expand='no')
        self.canvas.create_image(0,0,anchor=NW,
                                 image=eval('glb.img%d' % slot))

        for i, y in [(0, 0.330), (1, 0.619)]:
            setattr(self, 'j%d' % i, Enet10baseT(self.card_frame,
                      fid="10Base-T-%d", port=i, orient=HW_LEFT,
                      status=STATUS_OFF, xwidth=15, xheight=12))
            getattr(self, 'j%d' % i).j45_frame.place(relx=0.52,
                               rely=y, anchor=CENTER)

        for i in range(len(xypos)):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), CLED(self.card_frame,
                          self.canvas, shape=ROUND, width=4, status=STATUS_ON,
                          relx=xpos, rely=ypos))

class C6C110_PSU(C6C110_CardBlank):
    def __init__(self, master, slot=0):
        self.img = PhotoImage(file='images/6c110_psu.gif')
        setattr(glb,  'img%d' % slot, self.img)
        self.width  = self.img.width()
        self.height = self.img.height()

	C6C110_CardBlank.__init__(self, master=master, width=self.width,
                                  height=self.height)
        xypos = [(10,63),(16,63)]
        
        self.canvas = Canvas(self.card_frame, width=self.width,
                             bd=0,highlightthickness=0,
                             height=self.height,selectborderwidth=0)
        self.canvas.pack(side="top", fill=BOTH, expand='no')
        self.canvas.create_image(0,0,anchor=NW,
                                 image=eval('glb.img%d' % slot))

        for i in range(len(xypos)):
            xpos,ypos = xypos[i]
            setattr(self, 'led%d' % (i+1), CLED(self.card_frame,
                          self.canvas, shape=ROUND, width=4, status=STATUS_ON,
                          relx=xpos, rely=ypos))

class C6C110_Chassis:
    def __init__(self, master):
	self.outer=Frame(master, borderwidth=0, bg=Color.PANEL)
	self.outer.forget()  # We won't display until all
                             # the widgets have been created

        self.img = PhotoImage(file='images/6c110_chassis.gif')
        self.width  = self.img.width()
        self.height = self.img.height()

        self.canvas = Canvas(self.outer, width=self.width,
                             height=self.height,selectborderwidth=0)
        self.canvas.pack(side="top", fill=BOTH, expand='no')

        self.canvas.create_image(0,0,anchor=NW, image=self.img)

	self.rack = Frame(self.outer, bd=0, width=self.width-84,
                          height=self.height-180,
                          bg=Color.CHASSIS, highlightthickness=0)
	self.rack.place(relx=0.081, rely=0.117, anchor=NW)

        incr = 325/9
        x = 0.0
        for i in range(12):
            if i in [0,1,2,3,4,5]:
                card =C6C110_FDDI(self.rack, slot=i)
                card.card_frame.place(x=x, y=0, anchor=NW)
            elif i in [6,7,8,9]:
                card =C6C110_ENET(self.rack, slot=i)
                card.card_frame.place(x=x, y=0, anchor=NW)
            else:
                card =C6C110_PSU(self.rack, slot=i)
                card.card_frame.place(x=x, y=0, anchor=NW)
            x = x + card.width

	self.canvas.bind('<Button-1>', self.animate)

    def animate(self, event):
	import random
	choice = random.choice(range(0, len(st_wid)-1))
        op     = random.choice(range(0, len(ops)-1))
	pstr = 'st_wid[%d].%s()' % (choice, ops[op])
	self.cobj = compile(pstr, 'inline', 'exec')
	self.rack.after(50, self.doit)

    def doit(self):
	exec(self.cobj)
	self.rack.after(50, self.animate(None))

class Chassis:
    def __init__(self, master):
	self.outer=Frame(master, width=540, height=650, 
		          borderwidth=2, bg=Color.PANEL)
	self.outer.forget()  # We won't display until all
                             # the widgets have been created

        self.inner=Frame(self.outer, width=490, height=650, 
		          borderwidth=2, relief=RAISED, bg=Color.PANEL)
        self.inner.place(relx=0.5, rely=0.5, anchor=CENTER)
        
	self.rack = Frame(self.inner, bd=2, width=325, height=416,
                          bg=Color.CHASSIS)
	self.rack.place(relx=0.985, rely=0.853, anchor=SE)

        incr = 325/9
        x = 0.0
        for i in range(9):
            if i == 0:
                card =ProcessorCard(self.rack, width=incr-1, height=414)
            elif i == 1:
                card =SwitchCard(self.rack, width=incr-1, height=414)
            elif i == 2:
                card =OC3Card(self.rack, width=incr-1, height=414)
            elif i == 3:
                card =E10BASETCard(self.rack, width=incr-1, height=414)
            elif i == 4:
                card =T3AccessCard(self.rack, width=incr-1, height=414)
            elif i > 4:
                card =FastSerialCard(self.rack, width=incr-1, height=414)
            else:
                card =CardBlank(self.rack, width=incr-1, height=414)

            card.card_frame.place(x=x, y=0, anchor=NW)
            x = x + incr

	self.img = PhotoImage(file='images/logo.gif')
	self.logo=Label(self.outer, image=self.img, bd=0)
	self.logo.place(relx=0.055, rely=0.992, anchor=SW)
	self.logo.bind('<Button-1>', self.animate)

        for x in [0.02, 0.98]:
            for y in [0.0444, 0.3111, 0.6555, 0.9711]:
                Screw(self.outer, base="gray50").screw_frame.place(relx=x,
                                                 rely=y, anchor=CENTER)

        self.psu1 = PowerSupply(self.inner)
        self.psu1.psu_frame.place(relx=0.99, rely=0.004, anchor=NE)
        self.psu2 = PowerSupply(self.inner)
        self.psu2.psu_frame.place(relx=0.65, rely=0.004, anchor=NE)

        self.psu2.led.turnoff()

        screen1 = Screen(self.inner, width=150, height=600, bg=Color.PANEL)
        screen1.screen_frame.place(relx=0.16, rely=0.475, anchor=CENTER)
        screen2 = Screen(self.inner, width=330, height=80, bg=Color.PANEL)
        screen2.screen_frame.place(relx=0.988, rely=0.989, anchor=SE)

    def animate(self, event):
	import random
	choice = random.choice(range(0, len(st_wid)-1))
        op     = random.choice(range(0, len(ops)-1))
	pstr = 'st_wid[%d].%s()' % (choice, ops[op])
	self.cobj = compile(pstr, 'inline', 'exec')
	self.rack.after(50, self.doit)

    def doit(self):
	exec(self.cobj)
	self.rack.after(50, self.animate(None))

