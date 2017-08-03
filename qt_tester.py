#! /usr/bin/env python
import urllib.request #default module for Python 3.X
import qt_config

url = 'https://ca1.qualtrics.com/API/v3/surveys'
header = {'X-API-TOKEN': qt_config.x_api_token}

req = urllib.request.Request(url,None,header) #generating the request object
handler = urllib.request.urlopen(req) #running the request object

print(handler.status) #print status code
print(handler.reason)