"""
Solutions to cartalk puzzlers
Author: Josh Langowitz
"""
def main():
    checkAllAges(8)
    checkTripleDoubles()
    findPalindrOdometer()

def findPalindrOdometer():
    """
    Finds 6-digit numbers such that:
    the last 4 digits are a palindrome
    when you add one, the last 5 digits are a palindrome
    when you add another one, the middle 4 digits are a palindrome
    and when you add another one, all 6 digits are a palindrome
    """
    for i in xrange(100000,1000000-3):
        if checkPalindrOdometer(i):
            print '%d works' %i

def checkPalindrOdometer(num):
    """
    Returns True if num behaves such that: 
    the last 4 digits are a palindrome
    when you add one, the last 5 digits are a palindrome
    when you add another one, the middle 4 digits are a palindrome
    and when you add another one, all 6 digits are a palindrome

    num: 6 digit number
    """
    str1=str(num)[2:]
    str2=str(num+1)[1:]
    str3=str(num+2)[1:5]
    str4=str(num+3)[:]
    if (is_palindrome(str1) and is_palindrome(str2) and is_palindrome(str3) and is_palindrome(str4)):
        return True
    return False

def checkTripleDoubles():
    """
    Searches word list for words with triple double letters
    """
    for line in open('words.txt'):
        word=line.strip()
        if isTripleDouble(word):
            print word

def isTripleDouble(word):
    """
    Checks if a word has 3 consecutive double letters

    word: a string
    """
    for i in xrange(len(word)-6):
        if (word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]):
            return True
    return False

def reverseAgeCheck(diff, times):
    """
    Determines if 2 people with a given age difference will have opposite ages times times

    diff: integer
    times: integer

    returns True if the people have reverse ages times times.
    """
    age1=diff+10
    age2=10
    counter=0
    for i in xrange(90-diff):
        if isReverse(age1,age2):
            counter+=1
        age1+=1
        age2+=1
    return counter==times

def isReverse(a,b):
    """
    checks if two 2-digit numbers are palindromes
    a,b: 2-digit integers
    """
    return((a/10==b%10) and (a%10==b/10))

def checkAllAges(times):
    """
    prints the ages that have age reversals times times

    times: integer
    """
    for i in xrange(99):
        if reverseAgeCheck(i,times):
            print "An age difference of %d has %d age reversals over a long human life" %(i,times)

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the last character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Checks if word is a is_palindrome
    Makes sure first and last letters are the same, then removes them and 
    checks again until the word has no more pairs of letters left to check
     
    word: string

    returns: True if string is a palindrome, else False
    """
    if first(word) != last(word):
        return False
    elif len(word)<4:
        return True
    else:
        return is_palindrome(middle(word))

def interleave(s1,s2):
    snew=''
    s1i=0
    s2i=0
    l1=len(s1)
    l2=len(s2)
    tot=l1+l2
    ratio=float(l1)/tot
    for i in xrange(1,tot+1):
        s1buffer=i*ratio-s1i-.5
        if s1buffer>0 and s1i<l1:
            snew+=s1[s1i]
            s1i+=1
        elif s2i<l2:
            snew+=s2[s2i]
            s2i+=1
        else:
            print "something went wrong"
if __name__ == '__main__':
    main()