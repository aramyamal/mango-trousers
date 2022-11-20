import numpy as np
#input: list of 2-element tuples, where each tuple is an interval.
#output: new list of 2-element tuples with overlapping intervals merged.
def merge_intervals(l):    
    l = list(zip(sorted([i[0] for i in l]), sorted([i[1] for i in l])))
    ind = np.where(np.diff(np.array(l).flatten()) <= 0)[0]
    ind = ind[ind % 2 == 1] #for ranges with same start as stop
    return np.delete(l, [ind, ind+1]).reshape(-1, 2)