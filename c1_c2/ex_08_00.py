# Prompt the user input numbers to construct a list and calculate the average of the list
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    try:
        value = float(inp)
    except:
        print('Error, please enter numeric input')
        continue
    numlist.append(value)
print('Input: ',numlist)

average = sum(numlist) / len(numlist)
print('The average is: ', average)

