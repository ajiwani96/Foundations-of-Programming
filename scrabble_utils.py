import doctest
import random
import board_utils
import dicts_utils

def display_rack(r):
    ''' (dict) -> None
    >>> display_rack({'a': 2, 'f': 1, 'g': 2, 'o': 1, 'z': 1})
    A A F G G O Z 
    >>> display_rack({'g': 2, 'k': 0, 'p': 4})
    G G P P P P 
    '''
    for k in r:
        for i in range(r.get(k)):
            print(k.upper(), end=" ")
    return None

def has_letters(r, s):
    ''' (dict, str) -> bool
    >>> r = {'a': 2, 'c': 1, 't': 1, 'i': 2, 'r': 1}
    >>> has_letters(r, 'cat')
    True
    >>> r == {'a': 1, 'i': 2, 'r': 1}
    True
    >>> r = {'a': 2, 'c': 1, 't': 1, 'i': 2, 'r': 1}
    >>> has_letters(r, 'tiara')
    True
    >>> r == {'i': 1, 'c': 1}
    True
    >>> r = {'a': 2, 'c': 1, 't': 1, 'i': 2, 'r': 1}
    >>> has_letters(r, 'track')
    False
    >>> r == {'a': 2, 'c': 1, 't': 1, 'i': 2, 'r': 1}
    True
    >>> has_letters(r, 'tract')
    False
    >>> r == {'a': 2, 'c': 1, 't': 1, 'i': 2, 'r': 1}
    True
    '''
    s_dict = dicts_utils.count_occurences(s)
    if dicts_utils.is_subset(s_dict, r):
        dicts_utils.subtract_dicts(r, s_dict)
        return True
    return False

def refill_rack(r, p, n):
    ''' (dict, dict, int) -> None
    >>> random.seed(5)
    >>> r1 = {'a': 2, 'k': 1}
    >>> b = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
    >>> refill_rack(r1, b, 7)
    >>> r1
    {'a': 2, 'k': 1, 's': 1, 'l': 1, 't': 1, 'n': 1}
    >>> b
    {'a': 1, 'e': 2, 'h': 1, 'l': 1, 'p': 2, 's': 2, 't': 1, 'z': 1}
    >>> r2 = {'e': 3, 'q' : 1, 'r' : 1}
    >>> refill_rack(r2, b, 8)
    >>> r2
    {'e': 3, 'q': 1, 'r': 1, 'z': 1, 's': 1, 'a': 1}
    >>> b
    {'e': 2, 'h': 1, 'l': 1, 'p': 2, 's': 1, 't': 1}
    >>> refill_rack(r2, b, 5)
    >>> r2
    {'e': 3, 'q': 1, 'r': 1, 'z': 1, 's': 1, 'a': 1}
    >>> b
    {'e': 2, 'h': 1, 'l': 1, 'p': 2, 's': 1, 't': 1}
    '''
    #While length of rack is less than n and there are more still letters in the pool.
    while len(dicts_utils.flatten_dict(r)) < n and len(dicts_utils.flatten_dict(p)) > 0:
        #Randomly selecting letter from flattened dict.
        l = random.choice(dicts_utils.flatten_dict(p))
        #Chosen letter removed from pool.
        subtraction_dict = {l: 1}
        dicts_utils.subtract_dicts(p, subtraction_dict)
        #Chosen letter added to rack.
        if l not in r:
            r[l] = 0
        r[l] += 1
    return None

def compute_score(str_list, point_dict, scrabble_dict):
    ''' (list, dict, dict) -> int
    >>> v = {'a': 1, 'p': 3, 'h': 2}
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = dicts_utils.create_scrabble_dict(w)
    >>> compute_score(['hippo', 'aa'], v, d)
    10
    >>> compute_score(['umami', 'zebra'], v, d)
    0
    >>> compute_score(['qi'], v, d)
    0
    '''
    score = 0
    for s in str_list:
        if not dicts_utils.is_valid_word(s, scrabble_dict):
            return 0
        score += dicts_utils.get_word_score(s, point_dict)
    return score

def words_on_board(board):
    ''' (dict) -> list
    >>> b = [['c', 'a', 't', ' '], [' ', ' ', 'r', ' '], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> words_on_board(b)
    ['cat', 'train']
    >>> b = [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> words_on_board(b)
    ['cat', 'art', 'aa', 'train']
    '''
    #A list of rows/columns to be searched is made.
    search_list = []
    for i in board:
        search_list.append(i)
    for i in range(len(board[0])):
        search_list.append(board_utils.get_vertical_axis(board, i))
    #Each row/column is searched for words. Those found are added to the word list.
    word_list = []
    for search_row in search_list:
        if search_row[0] != ' ' and search_row[1] != ' ':
            word_list.append(board_utils.find_word(search_row, 0))
        for j in range(1, len(search_row)-1):
            if search_row[j-1] == ' ' and search_row[j] != ' ' and search_row[j+1] != ' ':
                word_list.append(board_utils.find_word(search_row, j))
    return word_list

def place_tiles(board, word, row_num, column_num, direction):
    ''' (list, str, int, int, str) -> list
    >>> b = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b, 'cat', 0, 0, 'right')
    ['cat']
    >>> b
    [['c', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b, 'rain', 1, 2, 'down')
    ['train']
    >>> b
    [['c', 'a', 't', ' '], [' ', ' ', 'r', ' '], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> words = place_tiles(b, 'at', 1, 1, 'right')
    >>> words.sort()
    >>> words
    ['aa', 'art']
    >>> b 
    [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> #The below will be testing things related to row id and mutability.
    >>> b2 = board_utils.create_board(5, 4)
    >>> b2
    [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> b3 = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> b2 == b3
    True
    >>> id(b2) == id(b3)
    False
    >>> b2[0] == b2[1]
    True
    >>> id(b2[0]) == id(b2[1])
    False
    >>> b3[0] == b3[1]
    True
    >>> id(b3[0]) == id(b3[1])
    False
    >>> place_tiles(b2, 'cat', 0, 0, 'right')
    ['cat']
    >>> b2
    [['c', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b3, 'cat', 0, 0, 'right')
    ['cat']
    >>> b3
    [['c', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    '''
    if direction != 'right' and direction != 'down':
        return []
    #A list is made of the words present at the beginning.
    preplace_word_list = words_on_board(board)
    #Placing of tiles:
    for l in word:
        while board[row_num][column_num] != ' ':
            if direction == 'right':
                column_num += 1
            if direction == 'down':
                row_num += 1
        board[row_num][column_num] = l   
    #A list is made of the words present at the end.
    postplace_word_list = words_on_board(board)
    #The lists are subtracted and returned.
    return list(set(postplace_word_list) - set(preplace_word_list))

def make_a_move(board, rack, word, row_num, column_num, direction):
    ''' (list, dict, str, int, int, str) -> list
    >>> b = [['c', 'a', 't', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> r = {'a': 3, 't': 2, 'c' : 1, 'r' : 1, 'i' : 1, 'n' : 1}
    >>> make_a_move(b, r, 'rain', 1, 2, 'down')
    ['train']
    >>> r == {'a': 2, 't' : 2, 'c' : 1}
    True
    >>> b
    [['c', 'a', 't', ' '], [' ', ' ', 'r', ' '], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> words = make_a_move(b, r, 'at', 1, 1, 'right')
    >>> words.sort()
    >>> words
    ['aa', 'art']
    >>> r == {'a': 1, 't' : 1, 'c' : 1}
    True
    >>> b
    [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> make_a_move(b, r, 'cats', 0, 2, 'right')
    Traceback (most recent call last):
    IndexError: Not enough space on the board.
    >>> r == {'a': 1, 't' : 1, 'c' : 1}
    True
    >>> b
    [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    '''
    #Checks valid direction. Otherwise, empty list.
    if direction != 'right' and direction != 'down':
        return []
    #Checks there's enough room to play those pieces. Otherwise, IndexError.
    if direction == 'right':
        if not board_utils.fit_on_board(board[row_num], word, column_num):
            raise IndexError("Not enough space on the board.")
    if direction == 'down':
        if not board_utils.fit_on_board(board_utils.get_vertical_axis(board, column_num), word, row_num):
            raise IndexError("Not enough space on the board.")
    #Checks the player has enough of the letters. Otherwise, ValueError.
    word_occurences = dicts_utils.count_occurences(word)
    if not dicts_utils.is_subset(word_occurences, rack):
        raise ValueError("Not enough letters in your rack.")
    #Removes letters from players rack.
    dicts_utils.subtract_dicts(rack, word_occurences)
    #Plays word on board and returns word list from place_tiles.
    return place_tiles(board, word, row_num, column_num, direction)
       
if __name__ == '__main__':
    doctest.testmod()