import transformer
import display
import input
import engine

init_board = '         '
players = ['X', '0']

def update_board(current_board, player, move):
    return current_board[:move] + player + current_board[move + 1:]

def play():
    moves = []

    # Get rotation factor from first move
    display.draw_grid(init_board)
    move = input.get_move(players[0]) - 1
    trans = transformer.transformer(move)
    move = trans.transform(move)
    current_board = update_board(init_board, players[0], move)
    moves.append(move)

    # Get rotation / reflection from second move
    move = engine.get_move(current_board)
    trans.set_reflection(move)
    move = trans.rotate(move) if trans.first_move == 4 else trans.reflect(move)
    current_board = update_board(current_board, players[1], move)
    moves.append(move)

    # Continue
    turn = 0
    player = 0
    winner = None
    while turn < 7 and winner == None:
        if player == 0:
            display.draw_grid(trans.undo_transformation(current_board))
            move = trans.transform(input.get_move(players[player]) - 1)
        else:
            move = engine.get_move(current_board)
        current_board = update_board(current_board, players[player], move)
        moves.append(move)
        winner = engine.check_winner(current_board)
        turn += 1
        player = (player + 1) % 2

    display.draw_grid(trans.undo_transformation(current_board))
    if winner != None:
        engine.update_weights(moves, (player + 1) % 2)
        print '\n{0} wins!'.format(winner)
