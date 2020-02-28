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
    if largest is None or fval > largest:
        largest = fval
    elif smallest is None or fval < smallest:
        smallest = fval
    #Find the largest and smallest value of user's input
print("Maximum: ",largest)
print("Minimum: ",smallest)