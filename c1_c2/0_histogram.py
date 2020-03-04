# Examples 1 

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('Words:',words)

print('Counting...')
for name in words :
# .get Method
    counts[name] =  counts.get(name,0) + 1

# IF - ELSE Method: 
#    if name not in counts :
#        counts[name] = 1
#    else :
#        counts[name] = counts[name] + 1

print('Counts:',counts)

# Eamples 2

scores = {'rico':1, 'liz':520, 'timo':100}
for key,value in scores.items() :
    print(key,value)

# Examples 3

fname = input('Enter the name of the files: ')
fhand = open(fname)
    # Made a Histogram of the words
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1
    # Find the word appeared the most often
bigword = None
bigcount = None
for word,count in counts.items() :
    if bigword is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, bigcount)