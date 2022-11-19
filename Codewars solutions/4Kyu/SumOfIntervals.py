#https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
import numpy as np

def merge_intervals(l):
    l = list(zip(sorted([i[0] for i in l]), sorted([i[1] for i in l])))
    ind = np.where(np.diff(np.array(l).flatten()) <= 0)[0]
    ind = ind[ind % 2 == 1] #filter ranges with same start as stop
    return np.delete(l, [ind, ind+1]).reshape(-1, 2)

def sum_of_intervals(intervals):
    return sum(x[-1] - x[0] for x in merge_intervals(intervals))
