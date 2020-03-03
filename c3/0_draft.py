import re

fname = input('Please enter the name of the files: ')
if len(fname) < 1 : fname = 'regex_sum_309952.txt'
fhand = open(fname)

print( sum( [ int(x) for x in re.findall('[0-9]+',fhand.read()) ] ) )




