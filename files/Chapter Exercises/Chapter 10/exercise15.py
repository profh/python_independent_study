# Chapter:		10
# Exercise:		15
# Start:		03:29:48 AM 07/01/2007
# End:			03:42:04 AM 07/01/2007
# Rating:		2
# Note:			Just shows how one class can reference another class
from graphics import *
   
from math import pi, sin, cos
from time import sleep

class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos


class Tracker:
	def __init__(self, window, objToTrack):
		self.window = window
		self.objToTrack = objToTrack
		self.circle = Circle(Point(self.objToTrack.getX(),self.objToTrack.getY()), 20)
		self.circle.setOutline("red")
		self.circle.draw(self.window)
		
	def update(self):
		self.circle.undraw()
		self.circle = Circle(Point(self.objToTrack.getX(),self.objToTrack.getY()), 20)
		self.circle.setOutline("red")
		self.circle.draw(self.window)

def main():
	win = GraphWin("Projectile", 400, 400)
	win.setCoords(-200, -20, 200, 400)
	angle = 140
	velocity = 120
	height = 0
	interval = 1
	p = Projectile(angle, velocity, height)
	t = Tracker(win, p)
	while p.getY() >= 0:
		p.update(interval)
		c = Circle(Point(p.getX(), p.getY()), 5)
		c.setFill("black")
		c.draw(win)
		t.update()
		print p.getY()
		sleep(0.005)
	
	win.getMouse()
		
	
main()

