# https://www.codewars.com/kata/52774a314c2333f0a7000688
def valid_parentheses(string):
    p_string = ''.join([x for x in string if x in '()'])
    while '()' in p_string:
        p_string = ''.join(p_string.split('()')) 
    return len(p_string) == 0
