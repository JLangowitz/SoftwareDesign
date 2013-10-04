"""
Author: Josh Langowitz
SofDes F2013 HW 5
"""

def main():
    print rotate('CHEER',59)
    print rotate('MELON',-10)

def rotate(s,n):
    """
    rotates a string s by n
    Deals with upper and lower case letters using a state variable
    Deals with wrap arounds by adding or subtracing 26 so the value is 
    back in a letter range

    s: string to be rotated
    n: amount to shift the string
    """
    n=n%26
    encrypt = ''
    for c in s:
        upper=False
        val=ord(c)
        if val<97:
            upper=True
            val+=32
        val+=n
        if val<97:
            val+=26
        if val>122:
            val-=26
        val-=upper*32
        encrypt+=chr(val)
    return encrypt

if __name__ == '__main__':
    main()