'''
Author: Josh Langowitz
Software Design F2013
HW 4 Dragon Curve
'''

from swampy.TurtleWorld import *
import math

def dragon(t,l,n):
    """
    Draws a dragon curve
    t: turtle object to draw with
    l: length of each segment
    n: number of iterations
    """
    fd(t,l)
    dragonRight(t,l,n)

def dragonRight(t,l,n):
    """
    Right hand logic for dragon
    """
    if n==0:
        return
    else:
        dragonRight(t,l,n-1)
        rt(t,90)
        dragonLeft(t,l,n-1)
        fd(t,l)
def dragonLeft(t,l,n):
    """
    Left hand logic for dragon
    """
    if n==0:
        return
    else:
        fd(t,l)
        dragonRight(t,l,n-1)
        lt(t,90)
        dragonLeft(t,l,n-1)

if __name__ == '__main__':
    world = TurtleWorld()
    bob = Turtle()
    bob.delay=.01
    print bob
    dragon(bob,10,10)

    wait_for_user()