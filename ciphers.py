import doctest
from crypto_helpers import *

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(s, k, m):
    ''' (str, int, int) -> str
    This function shift the entire string forward (if m == 1) k spots or backwards
    (if m == -1) k spots.
    >>> caesar('abc', 10, 1)
    'klm'
    >>> caesar('wtaad', 15, -1)
    'hello'
    >>> caesar('apple', -2, 1)
    'ynnjc'
    >>> caesar('cats and dogs', 5, 1)
    'hfyx fsi itlx'
    >>> caesar('hello', 11, 5)
    <class 'ValueError'>
    '''
    #If m is not 1 or -1, a ValueError is returned.
    if m != 1 and m != -1:
        return ValueError
    #If m is -1, k is made -k so it is shifted backwards.
    if m == -1:
        k = -k
    #An empty output string is created.
    output_string = ''
    #In a loop, each character is shifted k spots and added to the output string.
    for i in s:
        output_string += shift_char(i, k)
    #The output string is returned.
    return output_string

def vigenere(s, k, m):
    ''' (str, str, int) -> str
    >>> vigenere('BaNAna', 'apple', 1)
    'bpclra'
    >>> vigenere('bpclra', 'apple', -1)
    'banana'
    >>> vigenere('elephants and hippos', 'rats', 1)
    'vlxhyaglj tfu aagphk'
    >>> vigenere('vlxhyaglj tfu aagphk', 'RATS', -1)
    'elephants and hippos'
    >>> vigenere('hello', 'cat', 5)
    <class 'ValueError'>
    '''
    #If m is not 1 or -1, a ValueError is returned.
    if m != 1 and m != -1:
        return ValueError
    #An empty output string is created.
    output_string = ''
    #A key string the length of the string s is created using pad_keyword.
    key_string = pad_keyword(k, len(s))
    #If type m is 1...
    if m == 1:
        #A loop is made where i goes from 0 to the end of the string.
        for i in range(0, len(s)):
            #The character in string s at position i is shifted as many spots as the
            #index of the character at position i in the key string and then added to
            #the output string.
            output_string += shift_char(s[i], char_index(key_string[i]))
    #If type m is -1...
    if m == -1:
        #A loop is made where i goes from 0 to the end of the string.
        for i in range(0, len(s)):
            #The character in string s at position i is shifted as many spots as the
            #index of the character at position i in the key string (but negative) and
            #then added to the output string.
            output_string += shift_char(s[i], -char_index(key_string[i]))
    #The output string is returned.
    return output_string

if __name__ == '__main__':
    doctest.testmod()