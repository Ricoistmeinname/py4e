# Excercise 12.1 - Scraping HTML Data with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
counts = list()
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    # Create a list with the text content (numbers) that found in each tag
    counts.append(tag.contents[0])
# Convert all the string to integer with in the list and sum it up    
print(sum(int(num) for num in counts))


# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_309954.html