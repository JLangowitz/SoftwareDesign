"""
Author: Josh Langowitz
SofDes F2013, HW 5
"""

import math
def main():
    print estimate_pi()-math.pi

def estimate_pi():
    """
    Uses Srinivasa Ramanujan's infinite series to estimate pi

    Returns an estimate of pi
    """
    k=0
    series=0
    while True:
        nextTerm = 2*math.sqrt(2)/9801*(math.factorial(4*k)*(1103+26390*k))/(math.factorial(k)**4*396**(4*k))
        series+=nextTerm
        if nextTerm<1e-15:
            break
        k=k+1
    return 1/series

if __name__ == '__main__':
    main()