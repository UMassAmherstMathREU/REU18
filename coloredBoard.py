def coloredBoard(col, size, a, b):
    board = [0,]*size
    columns = [0,]*size
    for x in range(len(board)):
        board[x] = columns
    for row in range(len(board)):
        for co in range(len(board[row])):
            board[row][co] = (a*row + b*co) % col
            print(board[row][co], end="")
            print(" ", end="")
        print('')


coloredBoard(3,30,2,7)