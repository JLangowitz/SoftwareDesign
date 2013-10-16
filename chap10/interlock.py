"""
SofDes interlock homework
Author:Josh Langowitz
"""


from bisect import *

def main():
    findInterlocks(5)


def findInterlocks(n):
    """
    Finds and prints all sets of words that are interlocks
    """
    wordList=makeWordList()
    for word in wordList:
        words=splitWord(word,n)
        if isInterlock(word,wordList,n):
            line=''
            for s in words:
                line+= s +' and '
            line= line[:-5]+ ' interlock to form %s' %word
            print line

def isInterlock(word,wordList,n):
    """
    Checks if word can be made of n interleaving words

    word: string
    wordList: list of words that are legal
    n: integer
    """
    words=splitWord(word,n)
    for word in words:
        if not isInList(word,wordList):
            return False
    return True

def isInList(word,wordList):
    """
    Checks if word is in wordList

    word: string
    wordList: list of strings
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

def splitWord(word,n):
    """
    returns a list of n strings that interleave into word

    word: string
    n:integer
    """
    wordsOut=['']*n
    index=0
    for char in word:
        wordsOut[index]+=char
        index=(index+1)%n
    return wordsOut

if __name__ == '__main__':
    main()

def makeWordList():
    """
    turns a text file into an array of words
    """
    wordFile=open('words.txt')
    wordList=[]
    for line in wordFile:
        wordList.append(line.strip())
    return wordList