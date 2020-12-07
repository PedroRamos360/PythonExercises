# Staying on a chess board

import random

def is_move_possible(move):
    if move[0] > 0 and move[1] > 0:
        return True
    else: 
        return False


def is_knight_on_board(x, y, k, cache={}):
    out_of_board_probability = 1
    moves = [(x, y)]
    for i in range(k):
        for move in moves:
            all_moves = []
            possible_moves = []
            move_x, move_y = move
            all_moves.append((move_x - 1, move_y - 2))
            all_moves.append((move_x - 2, move_y - 1))
            all_moves.append((move_x + 2, move_y - 1))
            all_moves.append((move_x - 2, move_y + 1))
            all_moves.append((move_x + 1, move_y - 2))
            all_moves.append((move_x - 1, move_y + 2))
            all_moves.append((move_x + 2, move_y + 1))
            all_moves.append((move_x + 1, move_y + 2))

            filter_object = filter(is_move_possible, all_moves)
            for possible_move in filter_object:
                possible_moves.append(possible_move)
            moves = []
            for possible_move in possible_moves:
                moves.append(possible_move)
            
            if possible_move != []:
                out_of_board_probability *= len(possible_moves)/len(all_moves)   
            else:
                out_of_board_probability *= 1/len(all_moves)
        
    return out_of_board_probability

print(is_knight_on_board(0, 0, 8))
# 0.25

# OBS: Só funciona para k=1