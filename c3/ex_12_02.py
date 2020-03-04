# Excercise 12.2 - Following Links in HTML Using BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Gretchen.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count:')
count = int(count)
pos = input('Enter position:')
pos = int(pos)

# Retrieve and follow all of the link in desire position
print('Retrieving:', url) # Retrieve the input URL
time = 0
    # 'while Loop' control how many times we repeat the retrieving process
while True:
    tags = soup('a')
    # the 'for loop' control the link's position
    for tag in tags[:pos]:
        # get the URL at input position
        keyurl = tag.get('href', None)
    print('Retrieving:', keyurl)
    html = urllib.request.urlopen(keyurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    time = time +1
    if time == count : break


# http://www.dr-chuck.com/page1.htm
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Gretchen.html