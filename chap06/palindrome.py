"""Module that provides is_palindrome.

Author of is_palindrome: Josh Langowitz
"""

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
