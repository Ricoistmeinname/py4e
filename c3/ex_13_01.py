# Exercise 13.1 - Extracting Data from XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_309956.xml'
print('Retrieving', url)
uhand = urllib.request.urlopen(url, context=ctx)

data = uhand.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

# Retrieve all the tag 'count'
counts = tree.findall('./comments/comment/count')
print('Count:', len(counts))

# Retrieve all of the text under the tag
lst = list()
i = 0
for count in counts:
    snum = counts[i].text
    lst.append(int(snum))
    i = i + 1
#print(lst)
# Sum up all the value in the list
print('Sum:', sum(lst))    



# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_309956.xml