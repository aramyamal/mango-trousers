# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python
from scipy.special import binom
def expand(expr):
    exponent, base = expr.split('^')[-1], expr.split('^')[0]
    base = base.strip('(').strip(')')

    if exponent == '0':
        return '1'
    elif exponent == '1':
        return base
    
    base = '+' + base if base[0] != '-' else base

    if base.count('+') == 2: # coefficient and constant are positive
        coefficient = base.split('+')[1][0:-1]
        variable = base.split('+')[1][-1]
        constant = base.split('+')[2]
    
    elif base.count('+') == 1 and base.count('-') == 1: # coefficient and constant are negative
        if base[0] == '-':
            coefficient = base.split('+')[0][0:-1]
            variable = base.split('+')[0][-1]
            constant = base.split('+')[-1]
        else:
            coefficient = base.split('-')[0][1:-1]
            variable = base.split('-')[0][-1]
            constant = '-' + base.split('-')[-1]

    elif base.count('+') == 0 and int(exponent)%2 != 0: # coefficient and constant are negative, with odd exponent
        coefficient = '-' + base.split('-')[1][0:-1]
        variable = base.split('-')[1][-1]
        constant = '-' + base.split('-')[-1]
        
    elif base.count('+') == 0 and int(exponent)%2 == 0: # coefficient and constant are negative, with even exponent
        coefficient = base.split('-')[1][0:-1]
        variable = base.split('-')[1][-1]
        constant = base.split('-')[-1]

    coefficient = '+' '1' if coefficient == '' else coefficient
    coefficient = int(coefficient) if coefficient not in ('+', '-') else coefficient
    constant = int(constant)
    exponent = int(exponent)



    expresion = ''
    for i in range(int(exponent)+1):
        if i == 0:
            if coefficient == 1:
                expresion += variable + '^' + str(exponent-i)
            else:
                expresion += str(coefficient**exponent) + variable + '^' + str(exponent-i)
        elif i == 1:
            expresion += '+' + str(int(constant*binom(int(exponent), i)*coefficient**(exponent-i))) + variable + '^' + str(exponent-i)
        elif i < exponent-1:
            expresion += '+' + str(int(constant**(i)*binom(int(exponent), i)*coefficient**(exponent-i))) + variable + '^' + str(exponent-i)
        elif i == exponent-1:
            expresion += '+' + str(int(constant**(i)*binom(int(exponent), i)*coefficient**(exponent-i))) + variable
        if i == int(exponent):
            expresion += '+' + str(int(constant**i))
        
    #replace +- with -
    expresion = expresion.replace('+-', '-')
    expresion = expresion.replace('^1', '')
    return expresion

print(expand("(5m+3)^4"))

#"625m^4+1500m^3+1350m^2+540m+81"