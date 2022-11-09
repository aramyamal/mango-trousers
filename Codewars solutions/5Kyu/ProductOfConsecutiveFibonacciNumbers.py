#https://www.codewars.com/kata/5541f58a944b85ce6d00006a

from math import sqrt

def productFib(prod: list):
    def F(n: int):
        current, prior, prior2 = 0, 0, 1
        for n in range(n):
            current = prior + prior2
            prior, prior2 = current, prior
        return current
            
    i = 0
    stop = False
    istrue = True
    
    while i < 200 and stop == False:
        if F(i) * F(i+1) == prod:
            stop = True
        elif F(i) * F(i+1) > prod:
            stop = True
            istrue = False
        i += 1
        
    return [F(i-1), F(i), istrue]