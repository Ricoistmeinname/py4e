# Method 2 - The Double Split Pattern with guardian
while True:
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
        break
    except:
        print("The following file does not exists:",fname)
        continue

for line in fhand:
    line = line.rstrip()
# Guardian - Method 1
#    if line == '' :
#        continue
    words = line.split()
# Guardian - Method 2
#    if len(words) < 1 :
#        continue
# Guardian in a compound statement
    if len(words) < 3 or words[0] != 'From' :
        continue
    email = words[1]
    pieces = email.split('@')
    host = pieces[1]
    print('Host name:',host)