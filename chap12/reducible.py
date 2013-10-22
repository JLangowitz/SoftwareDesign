def main():
    answers=[]
    for word in wordSet:
        if isReducible(word, wordSet):
            answers.append((len(word),word))
    answers.sort()
    print answers[-1][1]

def isReducible(s,wordSet):
    """
    checks if s is reducible by recursively checking its substrings

    s: word
    wordSet: set of words in english dictionary
    """
    if s in memo:
        return memo[s]
    if s=='':
        memo[s]=True
        return True
    if s not in wordSet:
        memo[s]=False
        return False
    for subS in [restOf(s,n) for n in xrange(len(s))]:
        if isReducible(subS, wordSet):
            memo[s]=True
            return True
    memo[s]=False
    return False

def restOf(s,n):
    """
    Returns s with index n removed

    s: string

    n: int
    """
    return s[:n]+s[n+1:]

def makeWordSet():
    """
    turns a text file into an array of words
    """
    wordFile=open('words.txt')
    wordSet=set()
    for line in wordFile:
        word=line.strip()
        wordSet.add(word)
    return wordSet

if __name__ == '__main__':
    wordSet=makeWordSet()
    wordSet.add('a')
    wordSet.add('i')
    memo={}
    main()