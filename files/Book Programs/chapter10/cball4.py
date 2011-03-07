# cball4.py
#   Simulation of the flight of a cannon ball (or other projectile)
#   This version uses a  separate projectile module file

from projectile import Projectile

def getInputs():
    a = input("Enter the launch angle (in degrees): ")
    v = input("Enter the initial velocity (in meters/sec): ")
    h = input("Enter the initial height (in meters): ")
    t = input("Enter the time interval between position calculations: ")
    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)        
    print "\nDistance traveled: %0.1f meters." % (cball.getX())

if __name__ == "__main__": main()

