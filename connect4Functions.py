from generalMaths import convert_to_number
from copy import deepcopy

def has_won(grid, wins):
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
    width = 7
    height = len(grid) // width
    while grid[width * (height - 1) + row - 1] != ' ':
        height -= 1
        if width * (height - 1) + row - 1 < 0:
            return 0
    return height

def play(player, row, grid, tokens):
    width = 7
    new_grid = deepcopy(grid)
    if row <= 0 or row > 7:
        return False
    height = len(new_grid) // width
    while new_grid[width * (height - 1) + row - 1] != ' ':
        height -= 1
        if width * (height - 1) + row - 1 < 0:
            return False
    new_grid[width * (height - 1) + row - 1] = tokens[player]
    return new_grid

def get_all_moves(grid, player):
    width = 7
    tokens = ["O", "X"]
    moves = []
    for i in range(width):
        moves.append(play(convert_to_number(player), i+1, grid, tokens))
    return moves
