#https://www.codewars.com/kata/51c8e37cee245da6b40000bd/
import re
def strip_comments(strng, markers):
    if markers == []: return strng
    return '\n'.join([re.split(r'|'.join([ '\\' + x for x in markers]), item)[0].rstrip() for item in strng.split('\n')])