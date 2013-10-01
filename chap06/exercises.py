"""
Chapter 6 exercises
Josh Langowitz
"""

def isPower(a,b):
"""
checks if a is a power of b

a: int
b: int

returns: True if a is a power of b, else false
"""
	if a == b:
		return True
	elif a%b:
		return False
	else:
		return isPower(a/b,b)

def gcd(a,b):
"""
calculates greatest common denominator of a and b

a: int
b: int

returns: gcd of a and b
"""
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

if __name__ == '__main__':
	print isPower(25,5)
	print isPower(64,2)
	print isPower(25,100)
	print isPower(26,5)
	print gcd(2,5)
	print gcd(2,2)
	print gcd(100,25)
	print gcd(22,44)
	print gcd(64,96)