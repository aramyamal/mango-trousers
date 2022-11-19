#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python
from math import prod

def persistence(n):
    n_list = [x for x in str(n)]
    i = 0
    while n > 9:  
        n = 1
        for y in n_list:
            n *= int(y)
        n_list = [x for x in str(n)]
        i += 1
    return i


def persistence2(n):
    i = 0
    while n > 9:
        n = prod(int(x) for x in str(n))
        i += 1
    return i


def persistence3(n): #as compact as i can go
    i = 0 
    while n > 9: n = prod(int(x) for x in str(n)); i +=1
    return i
