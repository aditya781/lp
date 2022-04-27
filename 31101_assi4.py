n = int(input("Enter the number : "))

def accept():
    board = []
    for i in range (n):
        t = []
        for j in range (n):
            t.append(0)
        board.append(t)
    return board
  
def display(board):
    print()
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    
def isSafe(board, row, col):
     # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
    
    
def solveNQ(board, col):
    if col>=n:
        return True
    
    for i in range(n):
        if isSafe(board, i, col) == True:
            board[i][col] = 1
            if solveNQ(board, col + 1) == True:
                return True
            board[i][col] = 0
            
    return False
    
    
def solve():
    board = accept()
    
    if solveNQ(board, 0) == False:
        print("solution not exists")
    else:
        display(board)
        
solve()
    