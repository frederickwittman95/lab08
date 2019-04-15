#!/usr/bin/env python
# coding: utf-8

# In[12]:


# User provides board size, N.
def getBoardSize():
    n = input("Please provide the dimension of the chessboard.")
    return int(n)

global N
N = getBoardSize()

def printSolution(board):
    print('')
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end=' ') 
        print('')

def verifyDiagonal(board, row, col):
    j = col
    i = row
    while (j>=0 and i>=0):
        if board[i][j] == 1: 
           return False
        i-=1
        j-=1

    j = col
    i = row
    while (i<N and j>=0):
        if board[i][j] == 1: 
            return False
        j-=1
        i+=1

def verifyRow(board, row):
    for i in range(N):
        if board[row][i] == 1:
            return False

def isSafe(board, row, col): 
  
    DiagonalCheck = verifyDiagonal(board, row, col)
    RowCheck = verifyRow(board, row)

    if DiagonalCheck == False or RowCheck == False:
        return False
  
    return True

# Credit to https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/ for inspiring my solution.
def solveNQUtil(board, col): 
    if col == N:
        printSolution(board)
        return True
    
    res = False
  
    for i in range(N): 
        if isSafe(board, i, col): 
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0 
            
    return res

# New function added here; initializes boards with the dimension provided by the user.
def boardInitializer():
    board = []
    for i in range(N):
        board.append([0] * N)
    return board

def solveNQ(): 
    board = boardInitializer()
    if(solveNQUtil(board, 0) == False):
        print("No solution exists for a board with dimension", str(N) + ".")

solveNQ()


# In[ ]:


def getBoardSize():
    n = input("Please provide the dimension of the chessboard.")
    return n

N = getBoardSize()
print(N)


# In[ ]:




