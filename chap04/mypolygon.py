'''
Author: Josh Langowitz
Software Design F2013
HW 3 TurtleWorld Exercises
'''

from swampy.TurtleWorld import *
from math import pi


def square(t):
	'''
	Draws a square of side length 100

	t: turtle object to move
	'''
	for i in xrange(4):
		fd(t,100)
		lt(t)

def polygon(t,n):
	'''
	Draws a polygon of side length 100 with n sides

	t: turtle object to move
	'''
	for i in xrange(n):
		fd(t,100)
		lt(t,360.0/n)

def circle(t,r):
	'''
	Draws a hectagon approximation of a circle with radius r

	t: turtle object to move
	r: radius of circle
	'''
	for i in xrange(100):
		fd(t,2*pi*r/100)
		lt(t,3.6)

def arc(t,r,angle):
	'''
	Draws an arc of angle of the kilogon approximation 
	of a circle with radius r

	t: turtle object to move
	r: radius of circle
	angle: angle of arc to move
	'''
	# lt(t,.18)
	for i in xrange(int(1000*angle/360.0)):
		fd(t,2*pi*r/1000)
		lt(t,.36)
		
if __name__ == '__main__':
	# square(bob)
	# polygon(bob,6)
	# circle(bob,50)
	world = TurtleWorld()
	bob = Turtle()
	bob.delay=.01
	print bob
	arc(bob,50,360)

	wait_for_user()