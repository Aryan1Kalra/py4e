import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url: ')
data=urllib.request.urlopen(url, context=ctx).read()
tree=ET.fromstring(data)

counts=tree.findall('.//count')
#Here counts is equivalent to cmnt in the xmlex.py file but instead of holding comments as a full object only count position are heald so need to find count in the loop straight up print item.text instead
sum=0
for item in counts:
    sum+=int(item.text)
print(sum)