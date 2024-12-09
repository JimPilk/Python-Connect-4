from connect4Functions import get_height, get_all_moves, has_won

def evaluate(position, wins):
    width = 7
    ev = 0
    for i in wins:
        seen = []
        all = []
        for j in i:
            all.append(position[j])
            if position[j] != ' ':
                seen.append(position[j])
        if len(seen) == 4:
            if not('O' in seen and 'X' in seen):
                if seen[0] == 'O':
                    ev += 2 ** 32
                else:
                    ev -= 2 ** 32
        elif len(seen) != 0:
            if not('O' in seen and 'X' in seen):
                if seen[0] == 'O':
                    ev += 4 ** len(seen)
                else:
                    ev -= 4 ** len(seen)

                for l in range(len(all)):
                    if all[l] == ' ':
                        diff = get_height(position, i[l] % width) - i[l] // width
                        if seen[0] == 'O':
                            ev -= 2 ** (diff - 2) / (4 - len(seen) + 1)
                        else:
                            ev += 2 ** (diff - 2) / (4 - len(seen) + 1)
    return ev

def minimax(position, wins, depth, alpha, beta, max_player):
    if depth == 0 or has_won(position, wins) != None:
        return [evaluate(position, wins), None]

    if max_player:
        maxEval = float('-inf')
        index = 0
        bestChild = None
        for child in get_all_moves(position, True):
            index += 1
            if child != False:
                eval = minimax(child, wins, depth - 1, alpha, beta, False)[0]
                if eval > maxEval:
                    maxEval = eval
                    bestChild = index
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return [maxEval, bestChild]

    else:
        minEval = float('inf')
        index = 0
        bestChild = None
        for child in get_all_moves(position, False):
            index += 1
            if child != False:
                eval = minimax(child, wins, depth - 1, alpha, beta, True)[0]
                if eval < minEval:
                    minEval = eval
                    bestChild = index
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return [minEval, bestChild]
