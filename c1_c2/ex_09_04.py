# Excercise 9.4 - Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

record = dict()
for line in fhand :
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        record[words[1]] = record.get(words[1], 0) + 1

bigsender = None
bigcount = None
for sender,counts in record.items() :
    if bigcount is None or counts > bigcount :       
        bigsender = sender
        bigcount = counts
print(bigsender, bigcount)





