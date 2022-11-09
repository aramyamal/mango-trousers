# https://www.codewars.com/kata/529bf0e9bdf7657179000008
def valid_solution(board):
    for i in range(9):              #check if the sum of all columns is 45
        if sum(board[i]) != 45:
            return False
    
    for j in range(9):              #check if the sum of all rows is 45
        row_sum = 0
        for i in range(9):
            row_sum += board[i][j]
        if row_sum != 45:
            return False
    
    for l in [0,3,6]:               #check if each of the 9 subsquares have a sum of 45
        for k in [0,3,6]:
            square_sum = 0
            for i in range(3):
                for j in range(3):
                    square_sum += board[i+l][j+k] 
            if square_sum != 45:
                return False   

    return True