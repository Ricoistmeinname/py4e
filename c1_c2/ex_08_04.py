#Excercise 8.4 - Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.
while True:
    try:
        fname = input('Enter file name: ')
        fhand = open(fname)
        break
    except:
        print('The following file does not exists: ',fname)
        continue

lst = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    pos = 0
    for i in words:
        if not words[pos] in lst:
            lst.append(words[pos])
        pos = pos + 1
lst.sort()
print(lst)