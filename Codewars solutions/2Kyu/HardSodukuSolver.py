#https://www.codewars.com/kata/5588bd9f28dbb06f43000085/train/python
import numpy as np

def return_duplicate_index(list):   #returns all indexes of duplicates except for 0-duplicates
    dup = {}
    for i,x in enumerate(list):
        dup.setdefault(x,[]).append(i)
    duplicate_index = [x for i,x in dup.items() if len(x) > 1 and i > 0]
    return duplicate_index

def sudoku_valifier(puzzle):
    puzzle = np.array(puzzle)
    duplicate_indices = []

    for i in range(9):
        for dup in return_duplicate_index(puzzle[i]):
            for dup_index in dup:
                duplicate_indices.append([i, dup_index])

    for j in range(9):
        for dup in return_duplicate_index(puzzle[:,j]):
            for dup_index in dup:
                duplicate_indices.append([dup_index, j])
    
    return duplicate_indices if duplicate_indices else None
        


def sudoku_solver(puzzle):
    return


def test(list):
     row = np.array(list)
     unique, unique_idx, unique_count = np.unique(row, return_inverse=True, return_counts=True)
     count_mask = unique_count > 1
     duplicate_ids = unique[count_mask]

     print(unique, unique_idx, unique_count, count_mask)

print(sudoku_valifier([
            [0, 0, 6, 1, 0, 0, 0, 0, 8], 
            [0, 8, 0, 0, 9, 0, 0, 3, 0], 
            [2, 0, 0, 0, 0, 5, 4, 0, 0], 
            [4, 0, 0, 0, 0, 1, 8, 0, 0], 
            [0, 3, 0, 0, 7, 0, 0, 4, 0], 
            [0, 0, 7, 9, 0, 0, 0, 0, 3], 
            [0, 0, 8, 4, 0, 0, 0, 0, 6], 
            [0, 2, 0, 0, 5, 0, 0, 8, 0], 
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]))
