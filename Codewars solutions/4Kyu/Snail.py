# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
import numpy as np

def snail(snail_map):
    smap = np.asarray(snail_map)
    slist = []
    while smap.size:                    #while the number of elements exist
        slist += smap[0].tolist()       #add the top row to list
        smap = np.rot90(smap[1:])       #remove the top row, then rotate matrix 90 degrees
    return slist

print(snail([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))