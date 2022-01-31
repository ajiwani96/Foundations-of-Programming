import doctest

def count_occurences(s):
    ''' (str) -> dict
    >>> count_occurences('banana')
    {'b': 1, 'a': 3, 'n': 2}
    '''
    output_dict = {}
    for l in s:
        if l not in output_dict:
            output_dict[l] = 0
        output_dict[l] += 1
    return output_dict

def flatten_dict(d):
    ''' (dict) -> list
    >>> d = {'b': 1, 'a': 3, 'n': 2}
    >>> flatten_dict(d)
    ['b', 'a', 'a', 'a', 'n', 'n']
    >>> d
    {'b': 1, 'a': 3, 'n': 2}
    >>> flatten_dict({'cat': 2, 'dog': 0, 'bunny': 3})
    ['cat', 'cat', 'bunny', 'bunny', 'bunny']
    '''
    output_list = []
    for s in list(d.keys()):
        for i in range(d.get(s)):
            output_list.append(s)
    return output_list

def get_word_score(s, d):
    ''' (str, dict) -> int
    >>> v = {'a': 5, 't': 3, 'n': -2}
    >>> get_word_score('cat', v)
    8
    >>> get_word_score('banana', v)
    11
    >>> v = {}
    >>> get_word_score('banana', v)
    0
    '''
    score = 0
    for l in s:
        if l in d:
            score += d.get(l)
    return score

def is_subset(d1, d2):
    ''' (dict, dict) -> bool
    >>> a = {'a': 2, 'c': 1}
    >>> b = {'a': 2, 'b': 1, 'c': 2}
    >>> c = {'a': 1, 'c': 3}
    >>> is_subset(a, b)
    True
    >>> is_subset(b, a)
    False
    >>> is_subset(a, c)
    False
    >>> d = {'t': 4, 'v': 2}
    >>> is_subset(a, d)
    False
    '''
    for l in d1:
        if l not in d2:
            return False
        if d1.get(l) > d2.get(l):
            return False
    return True

def subtract_dicts(d1, d2):
    ''' (dict, dict) -> bool
    >>> a = {'a': 2, 'c': 1}
    >>> b = {'a': 2, 'b': 1, 'c': 2}
    >>> c = {'a': 5, 'b': 3}
    >>> subtract_dicts(b, a)
    True
    >>> b == {'b': 1, 'c': 1}
    True
    >>> subtract_dicts(c, a)
    False
    >>> c == {'a': 5, 'b': 3}
    True
    '''
    if is_subset(d2, d1):
        removal_list = []
        for l in d1:
            if l in d2:
                d1[l]-=d2.get(l)
                if d1[l] == 0:
                    removal_list.append(l)
        for i in removal_list:
            d1.pop(i)
        return True
    else:
        return False
      
def create_scrabble_dict(l):
    ''' (list) -> dict
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> create_scrabble_dict(w)
    {2: {'a': ['aa'], 'q': ['qi'], 'z': ['za']}, 3: {'c': ['cat', 'can', 'cow'], 'd': ['dog', 'dad']}, 5: {'h': ['hippo'], 'u': ['umami', 'uncle']}}
    '''
    output_dict = {}
    for s in l:
        if len(s) not in output_dict:
            output_dict[len(s)] = {}
        if s[0] not in output_dict[len(s)]:
            output_dict[len(s)][s[0]] = []
        output_dict[len(s)][s[0]].append(s)
    return output_dict

def is_valid_word(s, d):
    ''' (str, dict) -> bool
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(w)
    >>> is_valid_word('hippo', d)
    True
    >>> is_valid_word('umcle', d)
    False
    >>> is_valid_word('zebra', d)
    False
    >>> is_valid_word('pear', d)
    False
    '''
    if len(s) not in d:
        return False
    if s[0] not in d[len(s)]:
        return False
    if s not in d[len(s)][s[0]]:
        return False
    return True
        
if __name__ == '__main__':
    doctest.testmod()