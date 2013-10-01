import math
from swampy.TurtleWorld import *
from mypolygon import *

def flower(t,r,p,pointAng):
    '''
    draws a flower with p petals with angles of pointAng
    at the tips, with the petal tips r from the center 
    of the flower

    t:turtle to move
    r:int distance from center to tip of petals
    p:int number of petals
    pointAng:angle defined by lines tangent to the arcs 
    forming a petal at the point of that petal
    '''
    flowerAng=360.0/p
    arcAng=pointAng                                     #Based on some trig
    arcRad=r/math.sqrt((2*(1-math.cos(math.radians(arcAng)))))  #Using law of cosines
    rt(t,pointAng/2)
    for i in xrange(p):
        arc(t,arcRad,arcAng)
        lt(t,180-pointAng)                              #Want complimentary angle
        arc(t,arcRad,arcAng)
        rt(t,2*arcAng+180-pointAng-flowerAng)             #Turn to position of next flower
    lt(t,pointAng/2)
if __name__ == '__main__':
    # square(bob)
    # polygon(bob,6)
    # circle(bob,50)

    world = TurtleWorld()
    bob = Turtle()
    bob.delay=.0001
    print bob
    flower(bob,100,12,30)
    flower(bob,100,12,45)
    flower(bob,100,12,90)
    flower(bob,100,12,180)

    wait_for_user()