# cball1.py
#   Simulation of the flight of a cannon ball (or other projectile)
#   This version is not modularized.

from math import pi, sin, cos

def main():
    angle = input("Enter the launch angle (in degrees): ")
    vel = input("Enter the initial velocity (in meters/sec): ")
    h0 = input("Enter the initial height (in meters): ")
    time = input("Enter the time interval between position calculations: ")
    
    radians = (angle * pi)/180.0
    xpos = 0
    ypos = h0
    xvel = vel * cos(radians)
    yvel = vel * sin(radians)
    while ypos >= 0:
        xpos = xpos + time * xvel
        yvel1 = yvel - 9.8 * time
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1

    print "\nDistance traveled: %0.1f meters." % (xpos)

main()
