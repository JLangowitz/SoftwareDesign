'''
Author: Josh Langowitz
Software Design F2013
HW 4 Koch Curve
'''

from swampy.TurtleWorld import *
from math import pi


def koch(t,x,angle):
	"""
	Draws a koch curve or koch-like curve
	t: turtle object to draw with
	x: max length of koch curve
	angle: angle to turn for koch curve
	"""
	if x<3:
		fd(t,x)
	else:
		koch(t,x/3,angle)
		lt(t,angle)
		koch(t,x/3,angle)
		rt(t,angle*2)
		koch(t,x/3,angle)
		lt(t,angle)
		koch(t,x/3,angle)

def kochFlake(t,x,angle):
	"""
	Draws a koch snowflake or koch-like snowflake
	by calling koch 3 times with a 120 degree turn in between each call.
	See documentation for koch for parameter descriptions
	"""
	for i in xrange(3):
		koch(t,x,angle)
		rt(t,120)

if __name__ == '__main__':
	world = TurtleWorld()
	bob = Turtle()
	bob.delay=.01
	print bob
	kochFlake(bob,3**5,90)

	wait_for_user()