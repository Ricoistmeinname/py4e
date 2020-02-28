#Excercise 7.1 - Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# and print the contents of the file in upper case
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The following file does not exists:",fname)
    quit()
#Validate if the file exist or not under the folder
for line in fh:
    #line = line.upper()
    #line = line.rstrip()
    #print(line)
    #or
    line = line.rstrip()
    print(line.upper())

    
