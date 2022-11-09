#https://www.codewars.com/kata/5e52946a698ef0003252b526
def automata(rules, initial, generations):
    current_gen = initial
    length = len(initial)
    step = len(rules[0])//2

    for generation in range(generations):
        next_gen = []
        
        for i in range(length):
            temp = current_gen * 3
            sub_list = temp[i + length - step: i + length + step + 1]
            if sub_list in rules:
                next_gen.append(1)
            else:
                next_gen.append(0)
        current_gen = next_gen

    return next_gen