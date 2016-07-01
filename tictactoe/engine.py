from string import maketrans
import fileinput
import re
import random

winning = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]

def load_data(file):
    datafile = open(file, 'r')
    data = datafile.read()
    datafile.close()
    return data

def convert_board_to_data_format(board):
    # current_board format: "0XX 0   X"
    # data format: "y x x 3 y 0 3 1 x"

    board_to_data = maketrans("0X ", "yx0")
    return board.translate(board_to_data)
    

def get_weights(current_board):
    num_moves = len(current_board.replace(' ', ''))
    data = load_data('data/weights_{0}'.format(num_moves))

    lookup = " ".join(convert_board_to_data_format(current_board)).replace("0", "-?\d+")
    row = re.findall(lookup, data)[0].split(" ")
    return [(i, int(row[i])) for i, c in enumerate(row) if c != 'x' and c != 'y']


def get_move(current_board):
    weights = get_weights(current_board)
    shifted_weights = [(ind, weight + (1 - min(y for _, y in weights))) for ind, weight in weights]
    return random.choice(sum([[x]*y for x,y in shifted_weights], []))

def check_winner(current_board):
    xs = [i for i, x in enumerate(current_board) if x == 'X']
    winners = sum(1 for x in winning if set(x).issubset(xs))
    if winners > 0:
        return 'X'

    os = [i for i, x in enumerate(current_board) if x == '0']
    winners = sum(1 for x in winning if set(x).issubset(os))
    if winners > 0:
        return '0'

def update_weight(moves, index, adj):
    moves[index] = int(moves[index]) + adj
    return ' '.join(map(str,moves))

def update_board(moves, index, player):
    moves[index] = player
    return ' '.join(moves)

def update_weights(moves, winner):
    adj = 1 if winner == 0 else -1
    board = '0 0 0 0 0 0 0 0 0'

    for i in range(len(moves)):
        filename = 'data/weights_{0}'.format(i)
        data = load_data(filename)
        lookup = board.replace("0", "-?\d+")
        row = re.findall(lookup, data)[0].split(" ")
        new_row = update_weight(row, moves[i], adj)
        for line in fileinput.input(filename, inplace=True): 
            line = re.sub(lookup, new_row, line.rstrip())
            print(line)
        board = update_board(board.split(" "), moves[i], 'x' if i % 2 == 0 else 'y')
        adj = -adj
