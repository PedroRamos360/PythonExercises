# Staying on a chess board

def is_move_possible(move):
    if move[0] > 0 and move[1] > 0:
        return True
    else: 
        return False


def is_knight_on_board(x, y, k, cache={}):
    all_moves = []
    possible_moves = []

    all_moves.append((x - 1, y - 2))
    all_moves.append((x - 2, y - 1))
    all_moves.append((x + 2, y - 1))
    all_moves.append((x - 2, y + 1))
    all_moves.append((x + 1, y - 2))
    all_moves.append((x - 1, y + 2))
    all_moves.append((x + 2, y + 1))
    all_moves.append((x + 1, y + 2))

    moves = filter(is_move_possible, all_moves)
    for move in moves:
        possible_moves.append(move)
    
    return len(possible_moves)/len(all_moves)

print(is_knight_on_board(0, 0, 1))
# 0.25

# OBS: Só funciona para k=1