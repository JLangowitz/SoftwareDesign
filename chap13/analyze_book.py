"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random
import bisect


def process_file(filename, skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency.

    hist: map from word to the number of times it appears

    returns: list of (word, frequency) pairs, sorted by frequency
    """
    t = []
    for key, value in hist.items():
        t.append((value,key))
    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency
    num: number of words to print
    """
    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[:num]:
        print word, '\t', freq


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries

    returns: new dictionary
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key]=d1[key]
    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(words, freqList):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    choice=random.randint(1,freqList[-1])
    index=bisect.bisect_left(freqList,choice)
    return words[index]
    

def cum_freq(hist, words):
    """
    Makes a list of cumulative frequencies of the words in the dictionary

    words: list of the dictionary keys, to keep them from being in some weird order
    from hash strangeness
    hist: dictionary of words to frequencies
    """
    res=[]
    count=0
    for word in words:
        count+=hist[word]
        res.append(count)
    return res

if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    print 'Total number of words:', total_words(hist)
    print 'Number of different words:', different_words(hist)

    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[0:20]:
        print word, '\t', freq

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print "The words in the book that aren't in the word list are:"
    for word in diff.keys():
        print word,

    wordList=hist.keys()
    freqList=cum_freq(hist, wordList)
    print "\n\nHere are some random words from the book"
    for i in range(100):
        print random_word(wordList,freqList),

