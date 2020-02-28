#Excercise 5.2 - Find the largest and smallest number of user's input
largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = int(sval)
    except:
        print("Invalid input")
        continue
    #Validate the input and covert it to floating-point value
    if largest is None:
        largest = fval
    if fval > largest:
        largest = fval
    if smallest is None:
        smallest = fval
    if fval < smallest:
        smallest = fval
    #Find the largest and smallest value of user's input
print("Maximum: ",largest)
print("Minimum: ",smallest)