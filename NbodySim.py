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

def direction(Object1,Object2):
    """Calculates direction from first object to second"""
    
    Object1.dx = Object2.x - Object1.x
    Object1.dy = Object2.y - Object1.y
      
    return (Object1.dx,Object1.dy)

def force(Object1,Object2):
    """Calculates the force between two objects"""
    
    r = distance(Object1,Object2)
    f = (G*Object2.m)/r

    Object1.ax = 0
    Object1.ay = 0
    
    Object1.ax += f*Object1.dx
    Object1.ay += f*Object1.dy
    
    return 'f,ax,ay',f,Object1.ax,Object1.ay

def NewPositionVelocity(object1,t):
    """Calculates the postition of the object on the next timestep"""

    object1.vx += object1.ax*t
    object1.vy += object1.ay*t

    object1.x = object1.vx*t##+0.5*object1.ax*t**2 #try without a?
    object1.y = object1.vy*t##+0.5*object1.ay*t**2
        
    return 'x,y',object1.x,object1.y

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
        
            print('1',NewPositionVelocity(object1,i), '2', NewPositionVelocity(object2,i))
            time.sleep(.05)
        
p = Object(0,0,10000000,1,0)
q = Object(0,20,10000000,0,0)


RunSim(p,q,10)

