from collections import Counter
from time import time
from copy import copy
from pprint import pprint

def main():
    oneWordAnagrams(wordCounterDict)
    # while True:
    #     word = raw_input('Input word to anagram:\n').replace(' ','').lower()
    #     t=time()
    #     if not word:
    #         break
    #     printAnswers(anagram(FrozenCounter(word),wordCounterDict))
    #     print time()-t

def oneWordAnagrams(wordCounterDict):
    """
    Prints one word anagram sets

    wordCounterDict: dictionary mapping counters to the words they anagram to
    """
    anagrams=[]
    for counter in wordCounterDict:
        length=len(wordCounterDict[counter])
        if length>1:
            anagrams.append((length,wordCounterDict[counter]))
    anagrams.sort()
    for anagram in anagrams:
        if len(anagram[1][0])==8:
            print anagram[1]


class FrozenCounter(Counter):
    """Hashable Counter class"""
    def __hash__(self):
        "Implements hash(self) -> int"
        try:
            # Check cache first to avoid rebuilding frozenset each time
            return self._hash
        except AttributeError:
            self._hash = hash(frozenset(self.items()))
            return self._hash
    def __ge__(self, counter):
        temp=copy(self)
        temp.subtract(counter)
        return all(temp[x]>=0 for x in temp)

    def isEmpty(self):
        return len(self)==0

def anagram(wordCounter, allCounters):
    """
    Finds all anagrams of wordCounter including multi word anagrams
    recursively anagrams all subCounters of wordCounter

    wordCounter: frozen counter of a word
    allCounters: iterable of legal counters
    """
    if wordCounter in memo:
        return memo[wordCounter]
    if wordCounter.isEmpty():
        return [[]]
    answerList=[]
    checked=[]
    subCounters=[counter for counter in allCounters if (wordCounter>=counter)]
    for subCounter in subCounters:
        if subCounter not in checked:
            newCounter=FrozenCounter(wordCounter - subCounter)
            checked.append(newCounter)
            for answer in anagram(newCounter,subCounters):
                answerList.append([subCounter]+answer)
    memo[wordCounter]=answerList
    return answerList
                
def makeWordCounters():
    """
    turns a text file into an array of words
    """
    wordFile=open('words.txt')
    wordList={}
    for line in wordFile:
        word=line.strip()
        val=wordList.get(FrozenCounter(word),[])
        val.append(word)
        wordList[FrozenCounter(word)]=val
    return wordList
           
def combineLists(t1,t2):
    """
    returns all combinations of concatenations of elements of t1 and t2

    t1,t2: lists of strings
    """
    res=[]
    for item1 in t1:
        for item2 in t2:
            res.extend([item1+' '+item2])
    return res

def combineListofLists(t):
    """
    returns all combinations of all concatenations of 1 string from each list of strings in t
    """
    res=t[0]
    for i in xrange(1,len(t)):
        res=combineLists(res,t[i])
    return res

def printAnswers(answerList):
    """
    Prints the first 50 anagrams, by number of words and alphabetically

    answerList:list of lists of counters that make up anagrams
    """
    anagramTuples=[]
    for answer in answerList:
        subList=[]
        for word in answer:
            subList.append(wordCounterDict[word])
        anagramList=combineListofLists(subList)
        subTuples=[]
        for anagram in anagramList:
            subTuples.append((len(anagram),anagram))
        anagramTuples.extend(subTuples)
    anagramTuples.sort()
    if len(anagramTuples)>50:
        anagramTuples=anagramTuples[:50]
    for tup in anagramTuples:
        print tup[1]

if __name__ == '__main__':
    wordCounterDict=makeWordCounters()
    memo={}
    main()
    