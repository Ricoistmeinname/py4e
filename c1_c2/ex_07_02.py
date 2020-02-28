#Excercise 7.2 - Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below
# Do not use the sum() function or a variable named sum in your solution
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The following file does not exists:",fname)
    quit()
#Validate if the file exist or not under the folder
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")
        total = total + float(line[pos+1:])
        count = count + 1
        #print(total)
        #print(count) 
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
print("Average spam confidence:",total/count)
#print("Done")