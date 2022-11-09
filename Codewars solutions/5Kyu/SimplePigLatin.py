#https://www.codewars.com/kata/520b9d2ad5c005041100000f
def pig_it(text):
    text_list = text.split(' ')
    piglatin_list = []
    
    for word in text_list:
        if word not in '!?.':
            piglatin_list.append(word[1:] + word[0] + 'ay')
        else:
            piglatin_list.append(word)
            
    return ' '.join(piglatin_list) 