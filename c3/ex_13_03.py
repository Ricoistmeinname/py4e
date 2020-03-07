# Exercise 13.3 - Using the GeoJSON API - Use a GeoLocation lookup API modelled after the Google API to look up some universities and parse the returned data.
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    # encode the user' input from Unicode to UTF-8 and add it to API
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    # Read and decode the files from python
    print('Retrieving', url)
    uhand = urllib.request.urlopen(url, context=ctx)
    data = uhand.read().decode()
    print('Retrieved', len(data), 'characters')
    # Covert it to JSON for parasing 
    try:
        js = json.loads(data)
    except:
        js = None
    # Debugging 
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    # Find the object dictionary and retrieve its value
    place_id = js['results'][0]['place_id']
    print('Place id', place_id)    


# South Federal University
# UW Madison