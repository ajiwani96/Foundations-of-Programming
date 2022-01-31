import doctest

def create_board(row_num, column_num):
    ''' (int, int) -> list
    >>> create_board(3, 3)
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    >>> create_board(2, 5)
    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    >>> create_board(0, 5)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    >>> a = create_board(3, 3)
    >>> a
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    >>> id(a[0]) != id(a[1])
    True
    >>> id(a[1]) == id(a[2])
    False
    '''
    if row_num <= 0 or column_num <= 0:
        raise ValueError("Inputs must be positive")
    board = []
    for i in range(row_num):
        line_list = []
        for j in range(column_num):
            line_list.append(' ')
        board.append(line_list)
    return board

def display_board(board):
    ''' (list) -> None 
    >>> b = [['q', 'r', 'a', 'b', 't'], [' ', 't', 'u', ' ', ' ']]
    >>> display_board(b)
        0   1   2   3   4   
      +-------------------+
    0 | Q | R | A | B | T | 
      +-------------------+
    1 |   | T | U |   |   | 
      +-------------------+
    '''
    x = len(board[0])
    y = len(board)
    print("    ", end="")
    for column in range(x):
        print(str(column) + "   ", end="")
    print("")
    for row in range(y):
        print("  +" + "-"*(4*(x-1)+3) + "+")
        print(str(row) + " | ", end="")
        for column in range(x):
            print(str(board[row][column].upper()) + " | ", end="")
        print("")
    print("  +" + "-"*(4*(x-1)+3) + "+")
    return None

def get_vertical_axis(board, n):
    ''' (list) -> list
    >>> get_vertical_axis([['q', 'r', 'a', 'b', 't'], [' ', 't', 'u', ' ', ' ']], 0)
    ['q', ' ']
    >>> b = [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> get_vertical_axis(b, 2)
    ['t', 'r', 'a', 'i', 'n']
    '''
    vertical_axis = []
    for row in board:
        vertical_axis += row[n]
    return vertical_axis

def find_word(board_line, i):
    ''' (list, int) -> str
    >>> find_word([' ', 'c', 'a', 't', ' '], 1)
    'cat'
    >>> find_word(['c', 'a', 't', ' '], 1)
    'cat'
    >>> find_word([' ', 'squi', '', 'rre', 'l'], 2)
    'squirrel'
    >>> find_word([' ', 'c', 'a', 't', ' ', 'a', 'p', 'p', 'l', 'e'], 7)
    'apple'
    '''
    start_index = i
    while board_line[start_index] != ' ' and start_index >= 0:
        start_index -= 1
    start_index += 1
    end_index = i
    while board_line[end_index] != ' ' and end_index < len(board_line):
        end_index += 1
        if end_index == len(board_line):
            break
    end_index -= 1
    output_str = board_line[start_index]
    while start_index != end_index:
        start_index += 1
        output_str += board_line[start_index]
    return output_str

def available_space(board_line, i):
    ''' (list, int) -> int
    >>> available_space(['a', ' ', ' ', 'b', ' '], 1)
    3
    >>> available_space(['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' '], 2)
    5
    '''
    space_count = 0
    for j in range(i, len(board_line)):
        if board_line[j] == ' ':
            space_count += 1
    return space_count

def fit_on_board(board_line, s, i):
    ''' (list, str, int) -> bool
    >>> a = ['a', ' ', ' ', 'b', ' ']
    >>> fit_on_board(a, 'cat', 1)
    True
    >>> a = ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    >>> fit_on_board(a, 'apple', 4)
    False
    >>> a = ['a', ' ', ' ', 'b', ' ', ' ', 'c', 'd', ' ']
    >>> fit_on_board(a, 'pear', 3)
    False
    '''
    return board_line[i] == ' ' and len(s) <= available_space(board_line, i)

if __name__ == '__main__':
    doctest.testmod()