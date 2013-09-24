"""Solution to an exercise in Think Python.

Author: Joshua Langowitz
Exercise 3.5
Creates any size n by m grid out of ASCII characters
"""
def rByCGrid(r,c):
	divLine = '+ - - - - '*c + '+\n'
	midLine = '|         '*c + '|\n'
	grid = (divLine+midLine*4)*r+divLine
	return grid
	
print rByCGrid(6,7)
