# Exercise 13.2 - Extracting Data from JSON
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_309957.json'
print('Retrieving', url)
uhand = urllib.request.urlopen(url, context=ctx)

data = uhand.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
    print('==== Failure To Retrieve ====')
    print(data)

#print(json.dumps(js, indent=4))

# Count how many object within the object 'comments'
print(len(js['comments']))

counts = list()
i = 0
for count in js['comments']:
    count = js['comments'][i]['count']
    counts.append(int(count))
    i = i + 1
#print(counts)

# Sum up all the value in the list
print('Sum:', sum(counts))  



# http://py4e-data.dr-chuck.net/comments_42.json 
# http://py4e-data.dr-chuck.net/comments_309957.json