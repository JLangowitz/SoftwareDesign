from bisect import *

def main():
    findReversePairFast()

def isInList(word,wordList):
    """
    Binary search for word in sorted list
    """
    index=bisect_left(wordList,word)
    return index<len(wordList) and wordList[index]==word

def makeWordList():
    """
    turns a text file into an array of words
    """
    wordFile=open('words.txt')
    wordList=[]
    for line in wordFile:
        wordList.append(line.strip())
    return wordList

def findReversePairFast():
    """
    Finds reverse pairs and prints them

    Uses bisect because the list is alphabetical
    """
    wordList=makeWordList()
    for word in wordList:
        drow=word[::-1]
        if isInList(drow,wordList):
            print '%s and %s are a reverse pair' %(word,drow)

# This is waaaaaaaaaaaaaaaaaaaaaaaaaaay too slow
def findReversePairSLOW():
    """
    Finds reverse pairs in word list and prints them
    """
    for line1 in open('words.txt'):
        word1=line1.strip()
        # print word1
        for line2 in open('words.txt'):
            word2=line2.strip()
            # print word2
            if checkReversePair(word1,word2):
                print "%s and %s are a reverse pair" %(word1,word2)
            # else:
                # print "%s and %s are not a reverse pair" %(word1,word2)

def checkReversePair(strA, strB):
    """
    returns if strA and strB are a reverse pair
    strA, strB: strings
    """
    return (len(strA)==len(strB) and is_palindrome(strA+strB))

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

if __name__ == '__main__':
    main()