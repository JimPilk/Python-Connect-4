from generalMaths import convert_to_number, convert_to_boolean, get_wins
from connect4Functions import play, has_won
from consoleDisplay import printGrid
from bot import minimax

width = 7
tokens = ['O', 'X']
grid = [' '] * width * 6
wins = get_wins(width, len(grid) // width)
winner = None
go = 1

guiSetting = 1
autoPlayers = [False, False]
autoTerms = ["Bot", "Human"]
depth = 6

if guiSetting == 1:
    printGrid(grid, width)

while winner == None:
    go += 1
    go %= 2
    print("Player " + tokens[go] + "s go (" + autoTerms[convert_to_boolean(autoPlayers[go])] + ")")

    if autoPlayers[go]:
        best = minimax(grid, wins, depth, float('-inf'), float('inf'), convert_to_boolean(go))
        move = best[1]
    else:
        if guiSetting == 1:
            move = int(input())

    turn = play(go, move, grid, tokens)
    if turn == False:
        print("Illegal move!\nPlease Try Again:")
        go += 1
    else:
        grid = turn

    winner = has_won(grid, wins)
    if guiSetting == 1:
        printGrid(grid, width)

print(winner, "has won the game!")
