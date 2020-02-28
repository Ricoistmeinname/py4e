# Excercise 3.1 - Write a program to prompt for a score between 0.0 and 1.0
score = input("Enter Score: ")
try:
    fs = float(score)
    if fs > 1:
        quit()
    if fs < 0:
        quit() 
except:
    print("Error, please enter a numeric value between 0.0 and 1.0!")
    quit()
#Validate both the type of the input and the range of the input

if fs >= 0.9:
    print("A")
elif fs >= 0.8:
        print("B")
elif fs >= 0.7:
        print("C")
elif fs >= 0.6:
        print("D")
elif fs < 0.6:
    print("F")   
#Compute the score based on the validated input