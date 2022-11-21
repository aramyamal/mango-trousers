#https://www.codewars.com/kata/5588bd9f28dbb06f43000085/train/python
#https://nidragedd.github.io/sudoku-genetics/

# generate initial population
# repeat
#     rank the solutions, and retain only the percentage specified by selection rate
#     repeat
#         randomly select two solutions from the population
#         randomly choose a crossover point
#         recombine the solutions to produce n new solutions
#         apply the mutation operator to the solutions
#     until a new population has been produced
# until a solution is found or the maximum number of generations is reached

import numpy as np
from random import randint

def return_duplicate_index(list):   #for a list: returns 1-d index of all duplicates except for 0-duplicates
    dup = {}
    for i,x in enumerate(list):
        dup.setdefault(x,[]).append(i)
    duplicate_index = [x for i,x in dup.items() if len(x) > 1 and i > 0]
    return duplicate_index


def sudoku_validifier(puzzle):      #returns all duplicates of sudoku board and the corresponding
    puzzle = np.array(puzzle)       #2d-index of each duplicate. Return example of 1 duplicate:
    duplicate_indices = []          #'[(3, 5), (6, 5)]'. 2 duplicates: '[(3, 5), (3, 8), (2, 8), (3, 8)]'.
                                    #Multiple of the same index occurs because duplicates in both row/column and/or square 
    for i in range(9):
        for dup in return_duplicate_index(puzzle[i]):
            for dup_index in dup:
                duplicate_indices.append((i, dup_index))

    for j in range(9):
        for dup in return_duplicate_index(puzzle[:,j]):
            for dup_index in dup:
                duplicate_indices.append((dup_index, j))

    for k in range(0,9,3): 
        for l in range(0,9,3):
            list = puzzle[k:k+3,l:l+3].flatten()
            for dup in return_duplicate_index(list):
                for dup_index in dup:
                    duplicate_indices.append((dup_index//3 + k, dup_index%3 + l))

    return duplicate_indices


def remove_fixed_indices(fix, bad):                                     #fix = list of fixed indices as '[(2,5), (3,7), ...].
    return [bad[x] for x in range(len(bad)) if bad[x][:-1] not in fix]  #bad = list of new boardnumbers as [(3,7,9), (2,5,9), ...]
                                                                        #where first two is index and third value is the number 

def sudoku_solver(puzzle):
    puzzle = np.array(puzzle)
    puzzle_sol = puzzle.copy()                  #array to modify
    constants_indices = []
    for i,j in np.ndindex(puzzle.shape):        #make a list with the indices that cannot be changed
        if puzzle[i,j] != 0:
            constants_indices.append([i,j])

    # counter = 0
    # while counter < 100000:
    #     new_elements_pos = []                       #create a list with lists, where each list is [i, j, 'new number'] picked randomly
    #     new_amount = 5                              #how many new numbers
    #     for x in range(new_amount):
    #         new_elements_pos.append([randint(0,8), randint(0,8), randint(1,9)])
        
    #     new_elements_pos = [new_elements_pos[x] for x in range(len(new_elements_pos)) if new_elements_pos[x][:-1] not in constants_indices]
    #     #removed all new numbers that coincide with the permanent ones

    #     for element in new_elements_pos:            #add the new elements
    #         puzzle_sol[element[0],element[1]] = element[2]

    #     wrong_elements = sudoku_validifier(puzzle_sol)  #find duplicates
    #     wrong_elements = [wrong_elements[x] for x in range(len(wrong_elements)) if wrong_elements[x][:-1] not in constants_indices]
    #     #remove all permanent numbers from wrong_elements

    #     for element in wrong_elements:            #add the new elements
    #         puzzle_sol[element[0],element[1]] = 0
        
    #     if 0 not in puzzle_sol:
    #         break

    #     counter += 1
    # return puzzle_sol
    
matrix = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8], 
            [0, 8, 0, 0, 9, 0, 0, 3, 0], 
            [2, 0, 0, 0, 0, 5, 4, 0, 0], 
            [4, 0, 0, 0, 0, 1, 8, 0, 0], 
            [0, 3, 0, 0, 7, 0, 0, 4, 0], 
            [0, 0, 7, 9, 0, 0, 0, 0, 3], 
            [0, 0, 8, 4, 0, 0, 0, 0, 6], 
            [0, 2, 0, 0, 5, 0, 0, 8, 0], 
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]

solution = [
            [3, 4, 6, 1, 2, 7, 9, 5, 8], 
            [7, 8, 5, 6, 9, 4, 1, 3, 2], 
            [2, 1, 9, 3, 8, 5, 4, 6, 7], 
            [4, 6, 2, 5, 3, 1, 8, 7, 9], 
            [9, 3, 1, 2, 7, 8, 6, 4, 5], 
            [8, 5, 7, 9, 4, 6, 2, 1, 3], 
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]
        ]

print(list(return_duplicate_index(np.array(matrix[1]))))
