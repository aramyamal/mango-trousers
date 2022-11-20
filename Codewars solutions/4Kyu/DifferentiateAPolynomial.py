#https://www.codewars.com/kata/566584e3309db1b17d000027/python
def differentiate(equation, point):
    equation = equation[0] + equation[1:].replace('-','+-')
    term_list = [i for i in equation.split('+')]
    component_list = []
    answer = 0

    for term in term_list:
        if '^' in term: component_list.append([item for item in term.split('x^')])
        elif 'x' in term: component_list.append([term[0:-1], 1])
        else: component_list.append([term, 0])

    for component in component_list:
        if component[0] == '': component[0] = '1'
        if component[0] == '-': component[0] = '-1'
        answer += int(component[0]) * int(component[1]) * int(point ** (int(component[1]) - 1))

    return answer