#https://www.codewars.com/kata/54b72c16cd7f5154e9000457/python
import re

MORSE_CODE= { 'A':'.-', 'B':'-...', 
                'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 
                'L':'.-..', 'M':'--', 'N':'-.', 
                'O':'---', 'P':'.--.', 'Q':'--.-', 
                'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-'}

def decode_bits(bits):
    matches = re.findall(r'1+|0+', bits.strip('0'))
    transmission_rate = min(len(match) for match in matches)
    return bits.strip('0').replace('0000000'*transmission_rate, '   ').replace('000'*transmission_rate, ' ').replace('111'*transmission_rate, '-').replace('0'*transmission_rate, '').replace('1'*transmission_rate, '.')

def decode_morse(morse_code):
    return ' '.join([''.join([MORSE_CODE[z] for z in y]) for y in [x.split(' ') for x in morse_code.strip().split('   ')]])

