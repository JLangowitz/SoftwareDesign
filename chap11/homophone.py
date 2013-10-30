import pronounce
from pprint import pprint

def main():
    wordList=makeWordList()
    wordSet=set(wordList)
    wordDict=pronounce.read_dictionary()
    works=[]
    for word in wordList:
        t=(word,word[1:],word[0]+word[2:])
        if areHomophones(wordDict,t):
            works.append(word)
    for answer in works:
        print '%s is a solution' %answer
    # for word in wordList:
    #     rotates=findRotatePairs(word,wordSet)
    #     for rotation in rotates:
    #         print '%s is %s rotated by %d' %(word, rotation[1], rotation[0])

def areHomophones(wordDict,t):
    """
    Returns true if every word in t is a word and is a homphone of the other words in t

    wordDict: phonetic dictionary
    t: list of strings
    """
    return all([word in wordDict for word in t]) and len(set([wordDict[word] for word in t]))==1 
    #makes sure all words are keys in the dictionary and then checks to see that they all have the same value in the dictionary
def findRotatePairs(word,wordList):
    """
    Finds all rotate pairs of word in wordlist and returns a list of tuples
    containing the amount of the rotation and the rotated version

    word: string
    wordList: set of words in dictionary
    """
    rotates=[]
    for n in xrange(1,26):
        rotation=rotate(word,n)
        if rotation in wordList:
            rotates.append((n,rotation))
    return rotates

def makeWordList():
    """
    turns a text file into an array of words
    """
    wordFile=open('words.txt')
    wordList=[]
    for line in wordFile:
        wordList.append(line.strip())
    return wordList

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