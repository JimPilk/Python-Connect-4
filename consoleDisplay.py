def printGrid(grid, width):
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
