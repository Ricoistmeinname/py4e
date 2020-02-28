#Excercise 5.1 - Compute the total, counts, and average of the user's input
num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

print("ALL DONE")    
print("Total:",tot,"Counts:",num,"Average:",tot/num)
