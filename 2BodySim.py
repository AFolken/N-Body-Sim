import math
import time

G = 6.674*10**-11
C = 2 #collision precision


class Object:
    """x,y coords; mass"""

    def __init__(self,x=0,y=0,m=0,vx=0,vy=0,ax=0,ay=0):
        self.x = x
        self.y = y
        self.m = m
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

def distance(Object1,Object2):
    """Calculates distance between Objects"""

    d = math.sqrt((Object1.x-Object2.x)**2 + (Object1.y-Object2.y)**2)
    
    return d

def objectinfo(object):
    return (round(object.x,2),round(object.y,2),round(object.m,2),round(object.vx,2),round(object.vy,2),round(object.ax,2),round(object.ay,2))

def direction(Object1,Object2):
    """Calculates direction from first object to second"""
    
    Object1.dx = Object2.x - Object1.x
    Object1.dy = Object2.y - Object1.y

    #normalize
    n = math.sqrt(Object1.dx**2 + Object1.dy**2)
    
    Object1.dx = Object1.dx/n
    Object1.dy = Object1.dy/n
    
    return (Object1.dx,Object1.dy)

def force(Object1,Object2):
    """Calculates the force between two objects"""
    
    r = distance(Object1,Object2)
    f = (G*Object2.m*Object1.m)/(r**2)

    Object1.ax = 0
    Object1.ay = 0
    
    Object1.ax += f*Object1.dx
    Object1.ay += f*Object1.dy
    
    return 'f,ax,ay',f,Object1.ax,Object1.ay


def NewPositionVelocity(object,t):
    """Calculates the postition of the object on the next timestep"""

    object.vx += object.ax*t
    object.vy += object.ay*t

    object.x += object.vx*t##+0.5*object1.ax*t**2 #try without a?
    object.y += object.vy*t##+0.5*object1.ay*t**2
        
    return 'x,y',round(object.x,4),round(object.y,4)

def RunSim(object1,object2,t):
    
    t = list(range(1,t)) #list of 1 through t by 1 (e.g. t = 5, t = 1,2,3,4,5)
    
    for i in t:

        if round(object1.x,C) == round(object2.x,C) and round(object1.y,C) == round(object2.y,C):
            print ("Collision")
            break
        else:
            
            distance(object1,object2)
            direction(object1,object2)
            force(object1,object2)

            distance(object2,object1)
            direction(object2,object1)
            force(object2,object1)

            NewPositionVelocity(object1,i)
            NewPositionVelocity(object2,i)
        
            print('p1',objectinfo(p1), 'p2', objectinfo(p2))
            time.sleep(.05)
        
p1 = Object(20,0,10000000,0,0)
p2 = Object(0,0,10000000,0,0)


RunSim(p1,p2,4)

