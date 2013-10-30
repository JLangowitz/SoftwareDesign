"""
HW 8 Chapter 14 Exercise 3
Josh Langowitz
Worked with: Brooks Willis
"""


import anagram_sets as ana
import shelve

def main():
    store_anagrams('anagramList')
    print read_anagrams('anagramList', 'listen')

def store_anagrams(filename):
    """
    builds an anagram list and then stores it with pickle, returning the string to get it back
    """
    d = shelve.open(filename)
    d.update(ana.all_anagrams('../chap11/words.txt'))

def read_anagrams(filename, word):
    """
    opens the stored dictionary and anagrams the specified word

    filename: shelf to look int
    word: word to anagram
    """
    d=shelve.open(filename)
    sig=ana.signature(word)
    return d[sig]

if __name__ == '__main__':
    main()