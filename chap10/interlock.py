"""
SofDes interlock homework
Author:Josh Langowitz
"""


from bisect import *

def main():
    findInterlocks()

def findInterlocks():
    """
    Finds and prints all sets of words that are interlocks
    """
    wordList=makeWordList()
    for word in wordList:
        words=splitWord(word)
        if isInterlock(word,wordList):
            print "%s and %s interlock to form %s" %(words[0],words[1],word)

def isInterlock(word,wordList):
    words=splitWord(word)
    return isInList(words[0],wordList) and isInList(words[1],wordList)

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

def splitWord(word):
    wordsOut=['','']
    index=0
    for char in word:
        wordsOut[index]+=char
        index=1-index
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