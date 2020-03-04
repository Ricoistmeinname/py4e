# Examples 1 - Sorted the dictionary based on key
di = {'a':10, 'b':1, 'c':22}
for k, v in sorted(di.items()):
    print(k, v)

# Examples 2 - Sorted the dictionary based on values
di = {'a':10, 'b':1, 'c':22}
lst = list()
for k, v in di.items() :
    lst.append((v,k))
lst = sorted(lst, reverse= True) # sorted from high to low
print(lst)

# Example 3
fname = input('Enter the name of the files: ')
if len(fname) < 1 : fname = "words.txt"
fhand = open(fname)
    # Made a Histogram of the words
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1
    # make a new list of tuples in value-key order
lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)
    # sorted the list based on the value and silice out the top 10
lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)

# List Comprehension
di = {'a':10, 'b':1, 'c':22}
lst = list()
    # for key, val in di.items() :
    #   newtup = (val, key)
    #   lst.append(newtup)
    #   lst = sorted(lst, reverse=True)
lst = sorted([(val, key) for key, val in di.items()], reverse=True)
