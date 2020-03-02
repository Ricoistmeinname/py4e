# Excercise 11.1 -  Read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re

fname = input('Please enter the name of the files: ')
if len(fname) < 1 : fname = 'regex_sum_309952.txt'
fhand = open(fname)

lst = list()

    # Method 1 - list comprehension 1.0
for line in fhand :
    #line = line.rstrip()
    #if not re.search('[0-9]+', line) : continue
    lst = lst + re.findall('[0-9]+', line)

print(sum(int(num) for num in lst))
    # without list comprehension
#tot = 0
#for num in lst :
#    tot = tot + float(num)
#print(tot)

    #Method 2 - one line of code - list conprehension ultra
print( sum( [ int(x) for x in re.findall('[0-9]+',fhand.read()) ] ) )


