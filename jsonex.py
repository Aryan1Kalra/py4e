import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url: ')
data=urllib.request.urlopen(url, context=ctx).read()
js=dict(json.loads(data))

#print(js)
#print(js['comments'])
sum=0
for i in js['comments']:
    sum+=int(i['count'])
print(sum)