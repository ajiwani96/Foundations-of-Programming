import doctest
import math

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def in_engl_alpha(s):
    ''' str -> bool
    This returns whether or not the input string is composed entirely of characters in
    the english alphabet
    >>> in_engl_alpha('d')
    True
    >>> in_engl_alpha('A')
    True
    >>> in_engl_alpha('Mitochondria')
    True
    >>> in_engl_alpha('')
    False
    >>> in_engl_alpha(' ')
    False
    >>> in_engl_alpha('this is my kitty')
    False
    '''
    #If the string is empty, False is returned.
    if len(s) == 0:
        return False
    #Each character in the list is looped through.
    for i in s:
        #If the character made lower case is not in the alphabet list, False is
        #returned.
        if i.lower() not in alphabet_list:
            return False
    #If false is not returned above, True is returned.
    return True

def char_index(c):
    ''' (str) -> int
    This helper function will return the index of a character in the alphabet. It was
    made to avoid repeated code in following functions. It is assumed that only valid
    characters (upper or lower case)will be input.
    >>> char_index('a')
    0
    >>> char_index('B')
    1
    >>> char_index('z')
    25
    '''
    #In a loop, it is checked if each position in the alphabet list is equal to c.
    #When this is true, i is returned.
    for i in range(len(alphabet_list)):
        if alphabet_list[i] == c.lower():
            return i

def shift_char(c, n):
    ''' (str, int) -> str
    This function shifts characters n places forward in the alphabet. It returns that
    character, but lower case. If a single character is not input, a ValueError is
    returned. If the single character input is not a letter, the input character is
    returned.
    >>> shift_char('a', 4)
    'e'
    >>> shift_char('B', 1)
    'c'
    >>> shift_char('h', -5)
    'c'
    >>> shift_char('$', 17)
    '$'
    >>> shift_char('g', 86)
    'o'
    >>> shift_char('o', -86)
    'g'
    >>> shift_char('o', 0)
    'o'
    >>> shift_char('mitochondria', 2)
    <class 'ValueError'>
    '''
    #If the input is more than one character long, a ValueError is returned,
    if len(c) != 1:
        return ValueError
    #The input character is made lower case.
    c = c.lower()
    #If character c is not in the alphabet list, c is returned.
    if c not in alphabet_list:
        return c
    #The alphabet list index (al_index) of the character to be returned is set as the
    #sum of the input integer and the current position of c found with the char_index
    #helper function.
    al_index = n + char_index(c)
    #To avoid an index error when returning a character from the list, 26 is
    #repeatedly subtracted from al_index in a while loop until it is inbetween 0 and
    #25 (inclusive).
    while al_index > 25:
        al_index -= 26
    #The same is done as above but if al_index is less than 1, 26 is added to it.
    while al_index < 0:
        al_index += 26
    #The character of the alphabet associated with that index is returned.
    return alphabet_list[al_index]

def get_keys(s):
    ''' (str) -> list
    This function makes a list containing the indices of each character in the string.
    A ValueError is returned if any of the characters are not English characters.
    >>> get_keys('ayo')
    [0, 24, 14]
    >>> get_keys('CuteCat')
    [2, 20, 19, 4, 2, 0, 19]
    >>> get_keys('')
    []
    >>> get_keys('b')
    [1]
    '''
    #An empty output dictionary is created,
    output_dict = []
    #Each character in the string is looped through.
    for c in s:
        #The character is made lower case.
        c = c.lower()
        #If the character is not in the alphabet list, a ValueError is returned.
        if c not in alphabet_list:
            return ValueError
        #Otherwise, the index is appended to the output dictionary.
        output_dict.append(char_index(c))
    #The output dictionary is returned.
    return output_dict

def pad_keyword(s, n):
    ''' (str, int) -> str
    This makes a string of length n that is repitions of string s.
    >>> pad_keyword('cat', 10)
    'catcatcatc'
    >>> pad_keyword('van', 8)
    'vanvanva'
    >>> pad_keyword('typical', 7)
    'typical'
    >>> pad_keyword('', 5)
    <class 'ValueError'>
    '''
    #If s is an empty string, a ValueError is returned.
    if len(s) == 0:
        return ValueError
    #The number of repeates of s needed is calculated by dividing n by the length of s
    #and taking the floor of it.
    num_of_repeats = math.floor(n/len(s))
    #The output string is set as string s repeated the necessary amount of times.
    output_str = s * num_of_repeats
    #The amount of additional characters needed is determined by subtracting the
    #length of the current output string from n.
    additional_chars = n - len(output_str)
    #String s is spliced to as many characters as determined above and added to the
    #end of the output_string.
    output_str += s[0:additional_chars]
    #The output string is returned for the user.
    return output_str

if __name__ == '__main__':
    doctest.testmod()