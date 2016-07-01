def print_vertical_grid():
    print '   |   |      ',

def print_row_with_entries(entries):
    print ' {0} | {1} | {2}    '.format(*entries),

def print_horizontal_grid():
    print '-----------   ',

def print_row(row, moves):
    print_vertical_grid()
    print_vertical_grid()
    print ''
    print_row_with_entries(moves)
    print_row_with_entries(row)
    print ''
    print_vertical_grid()
    print_vertical_grid()

def draw_grid(current_board):
    print '\n'
    for row in range(3):
        moves = current_board[row*3:(row + 1)*3]
        print_row(range(row*3+ 1, row*3 + 4), moves)
        if row < 2:
            print ''
            print_horizontal_grid()
            print_horizontal_grid()
            print ''
