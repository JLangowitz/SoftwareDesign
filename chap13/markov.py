"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random
import pprint

def process_file(filename, skip_header=True, prefLen=2):
    """Makes a prefix map that contains the Markov prefixes mapped to words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each Markov prefix (tuple) of prefLen
    to the words that can come after it (list).
    """
    prefMap = {}
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)
    prefix=() #empty tuple because prefixes will be tuples
    for line in fp:
        #first prefix of next line is last prefix of previous line
        prefix=process_line(line, prefMap, prefix, prefLen)
    return prefMap


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, prefMap, prefix, prefLen):
    """Adds the prefix-suffix pairs in the line to the prefix map.

    Modifies prefMap.

    line: string
    prefMap: prefix map (map from prefix to words)

    returns: last prefLen words of the line for use as the next prefix
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip('_'+string.whitespace)
        # word = word.lower()

        # update the prefix map
        prefMap[prefix] = prefMap.get(prefix, [])+[word]

        #update the prefix for next iteration
        prefix=prefix[1-prefLen:]+(word,)
    return prefix


def random_word(prefMap, prefix):
    """Chooses a random word from a prefix map.

    The probability of each word is proportional to its frequency.
    """
    return (random.choice(prefMap[prefix]),)
    #returns a one element tuple for type matching
    


if __name__ == '__main__':
    PREF_LEN = 2 #constant for prefix length

    prefMap = process_file('emma.txt', skip_header=True, prefLen=PREF_LEN)
    
    # pprint.pprint(prefMap)
    print 'Here is some random text using Markov analysis on Emma'
    randText=random.choice(prefMap.keys())
    for i in xrange(500):
        prefix=randText[-PREF_LEN:]
        randText+=random_word(prefMap, prefix)
    print ' '.join(randText)