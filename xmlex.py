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

cmnt=tree.findall('comments/comment')
sum=0
for item in cmnt:
    sum+=int(item.find('count').text)
print(sum)