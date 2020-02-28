#Excercise 6.2 - Write code using find() and string slicing to extract the number at the end of the line below
#and Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
#print(text)
pos = text.find(":")
#print(pos)
snum = float(text[pos+1:].strip())
print(snum)