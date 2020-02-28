# Excercise 8.5 - Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line: 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.  Hint: make sure not to include the lines that start with 'From:'.

#  Easy way to open the required file:
#fname = input("Enter file name: ")
#if len(fname) < 1 : 
#    fname = "mbox-short.txt"
#fhand = open(fname)

while True:
    try:
        fname = input('Enter file name: ')
        fhand = open(fname)
        break
    except:
        print('The following file does not exists: ',fname)
        continue

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        count = count + 1
        print(words[1])

print("There were", count, "lines in the file with From as the first word")



