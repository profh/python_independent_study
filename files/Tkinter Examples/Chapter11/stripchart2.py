from Tkinter import *
from ftplib import *
import Pmw
import string, time, os
import thread
import AppShell
from PanelComponents import LED
from Common import SQUARE

from testdata import testData

####################################################################
# Constants
####################################################################

TEMP  = 1
PRESS = 2
SPEED = 3
HUM   = 4
VISIB = 5
DIR   = 6
CLOW  = 7
CHGH  = 8

BLANK_VALUE     = -123321

ALARMUNDER      = 0
ALARMOVER       = 1
WARNUNDER       = 2
WARNOVER        = 3

ALARM_STATUS	= "alarm"
WARNING_STATUS	= "warn"
ON_STATUS	= "turnon"
OFF_STATUS	= "turnoff"

noaa_url  = "weather.noaa.gov"
metar_dir = "/data/observations/metar/stations/"
temp_dir  = "/Temp"

digits = '0123456789'

####################################################################
# Weather Monitor
####################################################################

class WeatherMonitor:
    def __init__(self, master=None, host='', width=900, height=600,
                 bd=1, indent=30, titlespace=20):

	self.cells = [
          (0,0,1, 'Temp', -10, 110, TEMP, ['Temp'], 'Degrees F',
           [-10,0,10,20,30,40,50,60,70,80,90,100]),
          (1,0,1, 'Pressure', 27, 32, PRESS, ['Press'],'Inches Hg.',
           [27,28,29,30,31,32]),
          (2,0,0.4, 'Wind Speed', 0, 100, SPEED, ['WSpeed'], 'MPH',
           [0,20,40,60,80,100]),
          (2,0.48,0.40,'Wind Direction', 0, 360, DIR, ['WDir'], 'Degrees',
           [0,90,180,270,360]),
          (0,1,1, 'Humidity', 0, 100, HUM, ['Humidity'],  'Percent',
           [0,20,40,60,80,100]), 
          (1,1,1, 'Visibility', 0, 50, VISIB,['Visibility'], 'Miles',
           [0,10,20,30,40,50]), 
          (2,1,0.40, 'Cloud High', 10, 100, CHGH, ['CHigh', 'CVHigh'],
           'Feet (K)',
           [10,25,50,75,100]),
          (2,1.48,0.40, 'Cloud Low', 0, 30, CLOW, ['CLow'], 'Feet (K)',
           [0,5,10,15,20,25])
          ]

	self.XAxisData = {
            '5 Minutes':     ([0,1,2,3,4,5], 'Min'), 
            '10 Minutes':    ([0,2,4,6,8,10], 'Min'),
            '30 Minutes':    ([0,5,10,15,20,25,30], 'Min'), 
            '1 Hour':        ([0,10,20,30,40,50,60], 'Min'),
            '12 Hours':      ([0,2,4,6,8,10,12], 'Hrs'),
            '24 Hours':      ([0,4,8,12,16,20,24], 'Hrs')
                         }

	self.usePoll        = []
	self.Sessions       = {}
	self.wStation       = 'KPVD'

 	self.monitor        = None

	self.Surround       = 'Gray10'
	self.Base           = 'Gray80'
        self.Graph          = 'Gray20'
	self.Line           = '#22ffdc'
	self.Axes           = 'MediumSeaGreen'
	self.Labels         = 'MediumSeaGreen'
	self.Titles         = 'DarkGoldenRod1'
	self.CrossHairsH    = '#006600'
	self.CrossHairsV    = '#008800'
	self.Threshold      = 'red2'
	self.Warning        = 'orange'

	self.master        = master
	self.indent        = indent
	self.titlespace    = titlespace
	self.xindent       = (indent/4)*3
	self.yindent       = indent/4
	self.width         = width+(3*indent)
	self.height        = height+(2*indent)+(2*titlespace)
	self.cellWidth     = self.width/3
	self.cellHeight    = self.height/2
	self.axisWidth     = self.cellWidth - self.indent
	self.axisHeight    = self.cellHeight - \
                             (self.indent+self.titlespace)
	self.displayItems  = '12 Hours'
	self.refreshRate   = 60
	self.plottedData   = 'PMMarker'

        self.gotData       = FALSE
        self.threadRunning = FALSE
        self.testIndex     = 0

	self.frame=Frame(master, height=self.height,
                         width=self.width, relief='raised',
                         bd=bd)
	self.frame.pack(fill=BOTH, expand=0)
	self.innerframe=Frame(master, height=40, width=self.width,
                              relief='raised',
                              bg=self.Base, bd=bd)
	self.innerframe.pack(side=BOTTOM, fill=X, expand=0)
	self.refresh=Pmw.ComboBox(self.innerframe,
             history=0,
             entry_state = 'disabled', labelpos = W,
             label_text = 'Refresh Rate:',
             selectioncommand = self.setDisplayRate,
	     scrolledlist_items=('Default','1 Minute','5 Minutes',
                                 '10 Minutes','30 Minutes'))
	self.refresh.pack(padx=3, pady=3, side=LEFT)
	self.refresh.selectitem('Default')
	self.selector=Pmw.ComboBox(self.innerframe,
	     entry_state = 'disabled', history=0,
	     label_text = 'Display:', labelpos = W,
             selectioncommand = self.setDisplayRange,
	     scrolledlist_items=('10 Minutes','30 Minutes','1 Hour',
                                 '12 Hours','24 Hours'))
	self.selector.pack(padx=3, pady=3, side=LEFT)
	self.selector.selectitem('12 Hours')
	self.station=Pmw.ComboBox(self.innerframe,
             entry_state = 'disabled',
             history=0, label_text = 'Station:', labelpos = W,
             selectioncommand = self.setStation)
	self.station.pack(padx=3, pady=3, side=LEFT)

        fd = open('stations.txt')
        dataIn = fd.readlines()
        fd.close()
        stationList = []
        for data in dataIn:
            stationList.append(data[:-1])   # remove trailing newline
        self.station.setlist(stationList)
        self.station.selectitem('KPVD Providence')

	self.setThreshold=Button(self.innerframe,
             text='Set Thresholds', takefocus=1,
             command=self.setTValues)
	self.setThreshold.pack(padx=3, pady=3, side=RIGHT)

	self.canvas=Canvas(self.frame, width=self.width,
             highlightthickness=0, height=self.height, bg=self.Surround)
	self.canvas.pack(side="top", fill='x', expand='no')

	self.canvas.create_line(0,self.cellHeight,self.width+1,
                                self.cellHeight,
				fill='gray40', width=2)
	self.canvas.create_line(self.cellWidth+1,0,self.cellWidth+1,
                                self.height+1,
				fill='gray40', width=2)
	self.canvas.create_line((2*self.cellWidth)+1,0,
                                (2*self.cellWidth)+1,self.height+1,
				fill='gray40', width=2)

	self.maxSpan          = None

	self.pollTime         = None  # Time for these data

        self.Temp             = None
        self.Press            = None
        self.WSpeed           = None
        self.Humidity         = None
        self.Visibility       = None
        self.WDir             = None
        self.CLow             = None
        self.CHigh            = None        
        self.CVHigh           = None        
        
        self.lastTemp         = (-999.0,-999.0)
        self.lastPress        = (-999.0,-999.0)
        self.lastWSpeed       = (-999.0,-999.0)
        self.lastHumidity     = (-999.0,-999.0)
        self.lastVisibility   = (-999.0,-999.0)
        self.lastWDir         = (-999.0,-999.0)
        self.lastCLow         = (-999.0,-999.0)
        self.lastCHigh        = (-999.0,-999.0)        
        self.lastCVHigh       = (-999.0,-999.0)        

 	self.thresholdChanged      = TRUE
        self.TempThreshold         = (BLANK_VALUE, WARNOVER)
        self.PressThreshold        = (BLANK_VALUE, WARNUNDER)
        self.WSpeedThreshold       = (BLANK_VALUE, WARNOVER)
        self.HumidityThreshold     = (BLANK_VALUE, WARNOVER)
        self.VisibilityThreshold   = (BLANK_VALUE, WARNUNDER)
        self.WDirThreshold         = (BLANK_VALUE, WARNUNDER)
        self.CLowThreshold         = (BLANK_VALUE, WARNUNDER)        
        self.CHighThreshold        = (BLANK_VALUE, WARNUNDER)
        self.CVHighThreshold       = (BLANK_VALUE, WARNUNDER)
        
        self.setup_plot()

    def setup_plot(self, restart=1):
	for xf, yf, af, label, low, high, dataType, datalist, \
                yAxisLabel, ticklist in self.cells:
	    x0=(self.cellWidth*xf)+self.xindent
	    x1=(self.cellWidth*xf)+self.xindent+self.axisWidth
	    y0=(self.cellHeight*yf)+self.yindent+self.titlespace+1
	    y1=(self.cellHeight*yf)+self.yindent+self.titlespace+\
                (self.axisHeight*af)+1
	    self.canvas.create_rectangle(x0,y0,x1,y1,
					 fill=self.Graph, outline="")
	    self.canvas.create_line(x0,y0,x0,y1,
				    fill=self.Axes, width=2)
            if low <= 0:
                spread=abs(low)+abs(high)
                yx=float((spread-abs(low)))/float(spread)*\
                    (self.axisHeight*af)+y0
                self.canvas.create_line(x0,yx,x1,yx,
                                        fill=self.Axes, width=2)

	    self.canvas.create_text(x1-2,y0-self.titlespace+2,
                               text=label, font=('Verdana', 12),
                               fill=self.Titles,anchor='ne')
	    self.canvas.create_text(x0+2,y0-self.titlespace+2,
                               text=yAxisLabel, font=('Verdana', 12),
                               fill=self.Titles,anchor='nw')

	    self.doYAxis(x0, x1, y0, af, low, high, ticklist)
	    self.doXAxis(x0, x1, y0, y1, label)
	    self.canvas.create_line(x0,y0,x1,y0,
				    fill=self.Axes, width=2)
	    self.canvas.create_line(x1,y0,x1,y1,
				    fill=self.Axes, width=2)
	    self.canvas.create_line(x0,y1,x1,y1,
				    fill=self.Axes, width=2)
	    self.doThresholds()

	self.baseTime         = time.time()
	self.setDisplayRange(self.displayItems)

	if restart:
	    self.doPlot()

    def doYAxis(self, x0, x1, y0, af, low, high, ticklist):
        if low <= 0:
            spread=abs(low)+abs(high)
        else:
            spread = high-low
	negcomp=self.calculate_negative_component(low, high)
	for tick in ticklist:
            tickV = tick
            tickL = `tick`
	    y=((float(spread-(tickV+negcomp))/float(spread))*\
               (self.axisHeight*af))+y0-1
	    self.canvas.create_text(x0-2,y, text=tickL,
                                    font=('Verdana', 8),
                                    fill=self.Axes, anchor='e')
	    if not tickV == 0:
	        self.canvas.create_line(x0,y,x0+4,y, fill=self.Axes,
                                        width=2)
		self.canvas.create_line(x0+4,y,x1,y,
                                       fill=self.CrossHairsH, width=1)

    def doXAxis(self, x0, x1, y0, y1, tag):
	intlist, label = self.XAxisData[self.displayItems]
	ltag = translate_spaces(tag,'_')
	self.canvas.delete(ltag)   # Remove previous scales
	incr = self.axisWidth / (len(intlist)-1)
	xt = x0
	for tick in intlist:
	    if xt > x0:
	        self.canvas.create_line(xt,y1,xt,y1-4,
                                        fill=self.Axes, width=2,
                                        tags=ltag)
		self.canvas.create_line(xt,y0,xt,y1-4,
                                        fill=self.CrossHairsV,
                                        width=1, tags=ltag)
	    self.canvas.create_text(xt,y1+5, text=tick,
                                    font=('Verdana', 8),
                                    fill=self.Axes, anchor='n',
                                    tags=ltag)
	    xt = xt + incr
	self.canvas.create_text(xt-(incr*2)+(incr/2),y1+2,
                                text=label, font=('Verdana', 12),
                                fill=self.Titles, anchor='n',
                                tags=ltag)

    def doThresholds(self):
	for xf, yf, af, label, low, high, dataType, datalist, \
                yAxisLabel, ticklist in self.cells:
	    for data in datalist:
		tag = '%sThreshold' % data
		self.canvas.delete(tag)   # Remove previous data...
		threshold, action = getattr(self, '%sThreshold'%data)  
		if not threshold == BLANK_VALUE:
		    x0=(self.cellWidth*xf)+self.xindent
		    x1=(self.cellWidth*xf)+self.xindent+self.axisWidth
	    	    y0=(self.cellHeight*yf)+self.yindent+self.titlespace+1
                    xa1 = x0 + (x1-x0)/10
                    xa2 = x0 + (x1-x0)/2
                    xa3 = x1 - (x1-x0)/10
                    if low <= 0:
                        spread=abs(low)+abs(high)
                    else:
                        spread = high-low
	            negcomp=self.calculate_negative_component(low, high)
		    factor = -2
		    if action in [WARNOVER, ALARMOVER]:
			factor = 2
		    yt=((float(spread-(threshold+negcomp))/float(spread))*\
                        (self.axisHeight*af))+y0-1
	            self.canvas.create_line(x0,yt,x1,yt, fill=self.Threshold,
                                     width=2, tags=tag)
	            self.canvas.create_line(x0,yt+factor,x1,yt+factor,
                                     fill=self.Warning, width=2, tags=tag)
                    for x in [xa1, xa2, xa3]:
                        self.canvas.create_line(x,yt+factor, x,yt+(factor*10),
                                                fill=self.Warning, width=2,
                                                tags=tag, arrow='first',
                                                arrowshape=(8,8,3))
	self.thresholdChanged = FALSE

    def doPlot(self):
	# Check for threshold value....
	if self.thresholdChanged:
	    self.doThresholds()

        if self.gotData:
            self.gotData       = FALSE
            self.threadRunning = FALSE
        else:
            if self.threadRunning:
                self.frame.after(1000, self.doPlot)   # Spin
                return
            else:
                self.threadRunning = TRUE
                self.gotData       = FALSE
                thread.start_new(self.getMETAR, (noaa_url,metar_dir,
                                                 self.wStation))
                self.frame.after(1000, self.doPlot)   # Spin
                return

        if self.report:
            self.decodeMETAR(self.report)
        self.pollTime = time.time()

	for xf, yf, af, label, low, high, dataType, datalist, \
                yAxisLabel, ticklist in self.cells:
	    x0=(self.cellWidth*xf)+self.xindent
	    x1=(self.cellWidth*xf)+self.xindent+self.axisWidth
	    y0=(self.cellHeight*yf)+self.yindent+self.titlespace+1
	    y1=(self.cellHeight*yf)+self.yindent+self.titlespace+\
                (self.axisHeight*af)+1
            if low <= 0:
                spread=abs(low)+abs(high)
            else:
                spread = high-low
	    negcomp=self.calculate_negative_component(low, high)

	    for data in datalist:
		dataPoint = getattr(self, '%s' % data)
		if dataPoint or dataPoint == 0.0:
		    if self.pollTime > self.maxSpan:
			self.canvas.delete(self.plottedData) # Remove previous
			self.baseTime = self.pollTime
			self.setDisplayRange(self.displayItems)
		    xfactor = float(self.axisWidth) / (self.maxSpan - \
                                                       self.baseTime)
		    xv = self.pollTime - self.baseTime
		    if not dataPoint == float(BLANK_VALUE):
			centerx = x0 + ((xv * xfactor)-1) +2
			centery=((float(spread-(dataPoint+negcomp))/\
                                  float(spread))*(self.axisHeight*af))+y0-1

			lastX, lastY = getattr(self, 'last%s' % data)
			if not lastY == -999.0:
			    if not lastX >= centerx:
			        self.canvas.create_line(lastX,lastY,centerx,
                                                        centery, width=2,
				 		        fill=self.Line,
                                                        tags=self.plottedData)
			pstr = 'self.last%s = (%d,%d)' % (data,centerx,centery)
			    
		    else:
			pstr = 'self.last%s = (-999.0,-999.0)' % data

		    #### Now, check for thresholds
		    if self.monitor:     # have to be present to win...
	   	        threshold, action = eval('self.%sThreshold' % data)    
		        if not threshold == BLANK_VALUE:
			    if dataPoint == float(BLANK_VALUE):
				self.monitor.set(data, OFF_STATUS, 0)
			    else:
				takeAction = FALSE
				if action in [WARNUNDER, ALARMUNDER]:
				    if dataPoint <= threshold:
					takeAction = TRUE
				else:
				    if dataPoint >= threshold:
					takeAction = TRUE
				if takeAction:
				    if action in [WARNUNDER, WARNOVER]:
					self.monitor.set(data,WARNING_STATUS,0)
				    else:
					self.monitor.set(data,ALARM_STATUS,1)  
					self.monitor.frame.bell()	
				else:
				    self.monitor.set(data, ON_STATUS, 0)
		else:
		    pstr = 'self.last%s = (-999.0,-999.0)' % data

		exec(pstr)

	drawinterval = 1000*self.refreshRate
	self.frame.after(drawinterval, self.doPlot)

    def setDisplayRange(self, display):
	doSetup = FALSE
	if not self.displayItems == display:
	    doSetup = TRUE
	self.displayItems = display
	[value, units] = string.splitfields(display, ' ')
	mult = 1
	if units[:1] == 'M':
	    mult = 60
	if units[:1] == 'H':
	    mult = 3600
	self.maxSpan  = self.baseTime + (string.atoi(value) * mult)
	self.canvas.delete(self.plottedData)   # Remove previous data...
	if doSetup:
            self.setup_plot(restart=0)

    def setDisplayRate(self, rate):
	newRate = 10
	if not rate == 'Default':
	    [value, units] = string.splitfields(rate, ' ')
	    mult = 1
	    if units[:1] == 'M':
		mult = 60
	    newRate = string.atoi(value) * mult
	self.set_refreshRate(newRate)
	self.baseTime      = time.time()
	self.setDisplayRange(self.displayItems)

    def setStation(self, station):
        self.wStation = station[:4]
        self.master.title("Weather Monitor (%s)" % self.wStation)
        
    def set_hardware_data(self, vendor):
	SSMIHW.set_hardware_data(vendor)

    def calculate_negative_component(self, low, high):
	if low < 0:
            negcomp = abs(low)
	elif low > 0:
	    negcomp = -low
        else: 
	    negcomp = low
	return negcomp

    def set_refreshRate(self, rate):
	self.refreshRate = rate

    def setTValues(self):
	self.tw = SetThresholdsScreen()
        self.tw.setParent(self)
        self.tw.setCurrentValues()
        self.tw.run()

    def getMETAR(self, url=noaa_url, directory=metar_dir,
                 station='KPVD'):

#       UNCOMMENT the next line to inject test data (saves the bandwidth!)
##        return self.getTestData()

        tmp = '%s/wtemp' % temp_dir

        if os.path.exists(tmp) == 1:
            os.remove(tmp)

        data = open(tmp,'w')

        try:
            ftp = FTP(url)
            ftp.login()            
            ftp.cwd(directory)
            ftp.retrbinary('RETR %s.TXT' % station, data.write)
            ftp.quit
        except:
            print 'FTP failed...'
               
        data.close()

        report = open(tmp, 'r')
        self.report = report.read()
        self.gotData = TRUE
        
    def decodeMETAR(self, report):
        self.Temp             = None
        self.Press            = None
        self.WSpeed           = None
        self.Humidity         = None
        self.Visibility       = None
        self.WDir             = None
        self.CLow             = None
        self.CHigh            = None

        station = dtime = wind = visib = runway = weather = temp = alt = '--'
        lines = string.split(report, '\n')
        data  = string.split(lines[1], ' ')
        station  = data[0]
        dtime    = data[1]
        if not data[2][0] in 'CSA':    # COR, AUTO, SPEC
            wind = data[2]
            next = 3
        else:
            wind = data[3]
            next = 4
        if data[next][-2:] == 'SM':
            visib    = data[next]
        else:
            next = next + 1  #SKIP
            visib    = data[next]
        next     = next + 1
        if data[next][0] == 'R':
            runway = data[next]
            next = next + 1
        if data[next][:2] in ['MI','BC','PR','TS','BL','SH','DR','FZ','DZ',
                              'IC','UP','RA','PE','SN','GR','SG','GS','BR',
                              'SA','FG','HZ','FU','PY','VA','DU','SQ','FC',
                              'SS','DS','PO']:
            weather = data[next]
            next    = next + 1
        cloud = []
        while 1:
            if data[next][:3] in ['SKC','SCT','FEW','BKN','OVC','TCC','CLR']:
                cloud.append(data[next])
                next = next + 1
            else:
                break

        temp = data[next]
        next = next + 1
        alt  = data[next]

        if not wind[:3] == 'VRB':
            self.WDir   = atoi(wind[:3])
        self.WSpeed     = atoi(wind[3:])*23.0/20.0
        if self.WDir == 0 and self.WSpeed == 0.0:
            self.WDir   = None    # Calm
            self.WSpeed = 0.0

        if len(cloud) == 1 or len(cloud) == 2 or len(cloud) == 3:
            if cloud[0] == 'CLR':
                self.CLow = None
            else:
                self.CLow = atoi(cloud[0][3:6])/10
        if len(cloud) == 2 or len(cloud) == 3:
            if cloud[1] == 'CLR':
                self.CLow = None
            else:
                self.CHigh = atoi(cloud[1][3:6])/10
        elif len(cloud) == 3:
            if cloud[2] == 'CLR':
                self.CLow = None
            else:
                self.CVHigh = atoi(cloud[2][3:6])/10
            
        self.Visibility = atoi(visib)
        t, dpC          = string.split(temp, '/')
        self.Temp       = (atoi(t)*(9.0/5.0))+32
        dpF             = (atoi(dpC)*(9.0/5.0))+32
        self.Humidity   = (dpF/self.Temp)*100
        self.Press      = eval('%s.%s' % (alt[1:3], alt[-2:]), _safe_env)
           
    def getTestData(self):
        try:
            retData = 'Date Time\n%s' % testData[self.testIndex]
            self.testIndex = self.testIndex + 1
        except IndexError:
            retData = None
            self.testIndex = 0
        return retData

##############################################################################
#  Monitor Bar
##############################################################################

class MonitorBar:
    def __init__(self, master=None, host='', width=600, height=50, bd=1):
	self.master = master
	self.width=width
	self.height=height
	self.host=host
	self.frame=Frame(master, height=self.height, width=self.width,
                         relief='raised', bg='gray20')
	self.frame.pack(fill=BOTH, expand=NO)
	left = 0.05

	for LL, LV in [('Temp', 'Temp'),('Altimeter','Press'),
                ('Wind','WSpeed'),('Humidity','Humidity'),('Ceiling','CLow')]:
            Label(self.frame, text=LL, bg='gray20', font=('Verdana',10,'bold'),
                  fg="gray90").place(relx=left, rely=0.06, anchor=N)
            setattr(self, '%sled'%LV, LED(self.frame, height=20, width=20,
                                 shape=SQUARE, status=1, bg='gray20'))
            getattr(self, '%sled'%LV).led_frame.place(relx=left, rely=0.7,
                                                  anchor=CENTER)
	    left = left + 0.15

    def set(self, led, state, blink):
        ledO = getattr(self, '%sled'%led)
        exec('ledO.%s()'%state)
        ledO.blinkstate(blink)

##############################################################################
# Set Thresholds Screen
##############################################################################

class SetThresholdsScreen(AppShell.AppShell):
    usecommandarea=1
        
    def createButtons(self):
        self.buttonAdd('Apply', helpMessage='Apply thresholds',
                       statusMessage='Apply thresholds',
                       command=self.applyThresholds)
        self.buttonAdd('Cancel', helpMessage='Close this window',
                       statusMessage='Close thresholds screen',
                       command=self.cancelThresholds)
        
    def createMain(self):
        self.fields = [
            ('Temp','Temp',[(' ',BLANK_VALUE),('None',BLANK_VALUE),
                  ('32',32),('50',50),('75',75),('100',100),('110',110)], 'F'),
            ('Altimeter','Press',[(' ',BLANK_VALUE),('None',BLANK_VALUE),
                  ('28.0',28.0),('28.5',28.5),('29.0',29.0),('30.0',30.0),
                  ('30.5',30.5),('31.0',31.0),('31.1',31.1)], 'In. Hg'),
            ('Wind Speed','WSpeed',[(' ',BLANK_VALUE),('None',BLANK_VALUE),
                  ('10',10),('20',20),('30',30),('40',40),('50',50),('60',60),
                  ('70',70),('80',80),('90',90)], 'MPH'),
            ('Humidity','Humidity',[(' ',BLANK_VALUE),('None',BLANK_VALUE),
                  ('25',25),('50',50),('75',75),('80',80),('90',90),
                  ('100',100)], '%'),
            ('Ceiling','CLow',[(' ',BLANK_VALUE),('None',BLANK_VALUE),
                  ('1000',1),('2000',2),('3000',3),('4000',4),
                  ('5000',5)], 'Feet')]

	self.DLookup =  { 'Alarm Over': ALARMOVER, 'Alarm Under': ALARMUNDER,
			  'Warn Over':  WARNOVER,  'Warn Under':  WARNUNDER,
			  'None':       WARNUNDER, ' ':           WARNUNDER }
	self.rDLookup = { ALARMOVER: 'Alarm Over',  ALARMUNDER: 'Alarm Under',
			  WARNOVER:  'Warn Over',   WARNUNDER: 'Warn Under'}

	pwidth  = self.root.winfo_reqwidth() - 100
	pheight = self.root.winfo_reqheight() - 100
		
	self.frame1 = self.createcomponent('frame1', (), None,
                                           Frame,
                                           (self.interior(),),
                                           height=pheight, width=pwidth,
                                           bd=1, relief='ridge')
	self.frame1.forget()
        
 	for col in [0, 5]:
 	    self.frame1.columnconfigure(col, minsize=30)
 	    self.frame1.rowconfigure(0, minsize=20)
        Label(self.frame1, text=' ').grid(row=0, column=0)

	row = 1
	for label, var, valueList,units in self.fields:
	    self.frame1.rowconfigure(row, minsize=20)
	    setattr(self, '%sL'%var, Label(self.frame1,text=label))
            getattr(self, '%sL'%var).grid(row=row, column=1, sticky="e",
                                          padx=2, pady=2)
            setattr(self, '%sVLookup'%var, {})
            setattr(self, '%srVLookup'%var, {})

	    itemList=[]
	    for vLabel, vValue in valueList:
                itemList.append(vLabel)
                getattr(self, '%sVLookup'%var)[vLabel] = vValue
                getattr(self, '%srVLookup'%var)[vValue] = vLabel

	    setattr(self, '%s'%var, Pmw.ComboBox(self.frame1,
                       scrolledlist_items=itemList, entry_width=7,
                       entry_state="normal"))
            getattr(self, '%s'%var).grid(sticky="e", row=row, column=2,
                                         padx=2, pady=2)
            setattr(self, '%sU'%var, Label(self.frame1, text=units))
            getattr(self, '%sU'%var).grid(sticky="e", row=row, column=3,
                                          padx=4, pady=2)
            setattr(self, '%sT'%var, Pmw.ComboBox(self.frame1,
                       scrolledlist_items=(" ","Alarm Over", "Alarm Under",
                                           "Warn Over", "Warn Under"),
                       entry_width=11, listheight=90, entry_state="normal"))
            getattr(self, '%sT'%var).grid(sticky="e", row=row, column=4,
                                          padx=2, pady=2)
	    row = row + 1

	row = row + 1
	self.frame1.rowconfigure(row, minsize=20)
	Label(self.frame1, text=' ').grid(row=row, column=0)
	self.frame1.pack(padx=5, pady=5, fill=BOTH, expand=YES)

    def createInterface(self):
        self.option_add('*Entry.font', ('Verdana', 10, 'bold'))
        self.option_add('*Listbox.font', ('Verdana', 10, 'bold'))
        AppShell.AppShell.createInterface(self)
        self.root.title('Set Thresholds')
        self.createButtons()
        self.createMain()

    def setParent(self, parent):
        self.parent = parent

    def cancelThresholds(self):
        self.parent.tw.root.destroy()

    def setCurrentValues(self):
        parent = getattr(self, 'parent')
	for label, var, valueList,units in self.fields:
	    cV, cD = getattr(parent, '%sThreshold'%var)
	    if not cV == BLANK_VALUE:
                getattr(self, '%s'%var).selectitem(getattr(self,
                                                    '%srVLookup'%var)[cV])
                getattr(self, '%sT'%var).selectitem(self.rDLookup[cD]),
	    else:
		getattr(self, '%s'%var).selectitem(" ")
                getattr(self, '%sT'%var).selectitem(" ")

    def applyThresholds(self):
        parent = getattr(self, 'parent')
	for label, var, valueList,units in self.fields:
            tV = getattr(self, '%s'%var).get()
            tD = getattr(self, '%sT'%var).get()
            if not tV or tV == " ": tV = "None"
            if not tD or tD == " ": tD = "None"
            setattr(parent, '%sThreshold'%var, (getattr(self,
                            '%sVLookup'%var)[tV], self.DLookup[tD]))
	    
	self.parent.doThresholds()    # OK, go and set them...
        self.setCurrentValues()
 	self.thresholdChanged = TRUE

    def reset(self):
        parent = getattr(self, 'parent')
	for label, var, valueList,units in self.fields:
            setattr(parent, '%sThreshold'%var, (BLANK_VALUE, WARNUNDER))

        self.parent.doThresholds()    # OK, go and set them...
        self.setCurrentValues()

def translate_spaces(instring, trans):
    res = ''
    for c in instring:
	if c == ' ' or c == '\t':
	    if trans != "":   #To remove spaces
		res = res + trans
	else:
	    res = res + c
    return (res)

def translate_underbars(instring):
    res = ''
    for c in instring:
	if c == '_':
	    res = res + ' '
	else:
	    res = res + c
    return (res)

# "Safe" environment for eval()
_safe_env = {"__builtins__": {}}

def atoi(strIn):
    result = 0
    s    = string.strip(strIn)
    sign = ''
    if s:
        if s[0] in '+-':
            sign = s[0]
            s = s[1:]
	while s[0] == '0' and len(s) > 1: s = s[1:]
        str = sign
	for c in s:
            if c not in digits:
                break   #  Got a terminator
            str = str + c
        if str:
            result = eval(str, _safe_env)
    return result

if __name__ == '__main__':

    root = Tk()
    root.option_add('*background', 'grey')
    root.option_add('*foreground', 'black')
    root.option_add('*Entry.background', 'white')
    root.option_add('*Label.background', 'grey')
    Pmw.initialise(root, fontScheme = 'pmw1', useTkOptionDb = 0)
    w = WeatherMonitor(root, width=720, height=430)
    w.master.title("Weather Monitor (%s)" % w.wStation)
    w.master.iconname('Weather')
    w.master.geometry('+20+20')
    top = Toplevel(root)
    w2 = MonitorBar(top)
    w.monitor=w2
    w2.master.title("Weather Threshold Monitor")
    w2.master.geometry('+20+650')
    
    root.mainloop()
