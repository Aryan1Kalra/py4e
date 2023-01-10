import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos=input('Position - ')
pos=int(pos)
i=input('Repeat- ')
i=int(i)
while(i>0):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    url=tags[pos-1].get('href')
    i-=1
print(tags[pos-1].contents[0])