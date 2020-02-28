# Excercise 10.2 - Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:') :
        hrs = line.split()        
        #hrs = hrs[5][:2]
        counts[hrs[5][:2]] = counts.get(hrs[5][:2], 0) + 1

lst = list()
lst = sorted([(key, val)for key, val in counts.items()])
#lst = sorted([(val, key) for key, val in counts.items()], reverse=True)  # sorted base on the value from high to low 
for key, val in lst :
    print(key, val)

# Without list comprehension method:
#lst = list()
#newtuple = tuple()
#for key, val in counts.items():
#    newtuple = (key, val)
#    lst.append(newtuple)
#lst.sort()
#for key, val in lst :
#    print(key, val)