fname = input("Enter the file name: ")
fhand = open(fname,'r')
count = 0
for line in fhand:
    if not line.startswith('Subject:'):
        continue
    count = count + 1
print('There were', count, 'subject lines in',fname)
