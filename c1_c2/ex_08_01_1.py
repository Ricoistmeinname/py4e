# Method 1 - The Double Split Pattern
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
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    host = pieces[1]
    print('Host name: ',host)

