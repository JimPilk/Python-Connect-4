import random
import copy

width = 7
tokens = ['O', 'X']
grid = [' '] * width * 6

def print_grid(grid):
    global width
    for i in range(len(grid) // width):
        for j in range(width):
            counter_index = i * width + j
            counter = str(grid[counter_index])
            print('|' + counter, end = '')
        print('|')
    print('—' * (width * 2 + 1))
    for i in range(width):
        print(' ' + str(i+1), end = '')
    print()
    
def get_wins(width, height):
    area = width * height 
    wins = []
    for i in range(area):
        
        if i // width >= 3:
            #veritcal
            temp = []
            for j in range(4):
                temp.append(i - width * j)
            wins.append(temp)
            
            if i % width >= 3:
                #top left
                temp = []
                for j in range(4):
                    temp.append(i - width * j - j)
                wins.append(temp)
            
            if i % width <= width - 4:
                #top right
                temp = []
                for j in range(4):
                    temp.append(i - width * j + j)
                wins.append(temp)
                
        if i % width <= width - 4:
            #right
            temp = []
            for j in range(4):
                temp.append(i + j)
            wins.append(temp)
            
    return wins
    
def has_won(grid, width):
    global wins
    for i in wins:
        seen = []
        for j in i:
            if grid[j] != ' ':
                seen.append(grid[j])
        if len(seen) == 4:
            if not('O' in seen and 'X' in seen):
                return seen[0]
    return None
            
def get_height(grid, row):
    global width
    height = len(grid) // width
    while grid[width * (height - 1) + row - 1] != ' ':
        height -= 1
        if width * (height - 1) + row - 1 < 0:
            return 0
    return height
            
def play(player, row, grid):
    global width
    new_grid = copy.deepcopy(grid)
    if row <= 0 or row > 7:
        return False
    height = len(new_grid) // width
    while new_grid[width * (height - 1) + row - 1] != ' ':
        height -= 1
        if width * (height - 1) + row - 1 < 0:
            return False
    new_grid[width * (height - 1) + row - 1] = tokens[player]
    return new_grid
    
def convert_to_number(boolean):
    if boolean:
        return 0
    return 1
    
def get_all_moves(grid, player):
    global width
    moves = []
    for i in range(width):
        moves.append(play(convert_to_number(player), i+1, grid))
    return moves

def evaluate(position):
    global wins
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
                        global width
                        diff = get_height(position, i[l] % width) - i[l] // width
                        if seen[0] == 'O':
                            ev -= 2 ** (diff - 2) / (4 - len(seen) + 1)
                        else:
                            ev += 2 ** (diff - 2) / (4 - len(seen) + 1)
    return ev
    
def minimax(position, depth, alpha, beta, max_player):
    global width
    if depth == 0 or has_won(position, width) != None:
        return [evaluate(position), None]
        
    if max_player:
        maxEval = float('-inf')
        index = 0
        bestChild = None
        for child in get_all_moves(position, True):
            index += 1
            if child != False:
                eval = minimax(child, depth - 1, alpha, beta, False)[0]
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
                eval = minimax(child, depth - 1, alpha, beta, True)[0]
                if eval < minEval:
                    minEval = eval
                    bestChild = index
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return [minEval, bestChild]

auto = True
tips = False
double = False
depth = 6
rand_start = 10
preset = 0
preset /= 2
wins = get_wins(width, len(grid) // width)
go = 69420
winner = None
print_grid(grid)
while winner == None:
    go += 1
    go %= 2
    print('Current evalutaion:', evaluate(grid))
    if rand_start > 0:
        move = random.randint(1, 7)
        rand_start -= 1
    else:
        if (auto == True or tips == True or double == True) and preset <= 0:
            if go == 0: 
                best = minimax(grid, depth, float('-inf'), float('inf'), True)
            elif auto == False:
                best = minimax(grid, depth, float('-inf'), float('inf'), False)
        if auto == False and tips == True and preset <= 0:
            print('Computer recomends row', best[1])
        if auto and go == 0 and preset <= 0 or (double and preset <= 0):
            move = best[1]
            print()
            print('The computer played row', move)
        else:
            print('Your go (' + tokens[go] + ')')
            move = int(input())
            preset -= 0.5
    if play(go, move, grid) == False:
        print('Illegal Move\nTry Again')
        go += 1
        go %= 2
    else:
        grid = play(go, move, grid)
    print()
    print_grid(grid)
    print()
    winner = has_won(grid, width)

print(winner, 'has won the game!')
