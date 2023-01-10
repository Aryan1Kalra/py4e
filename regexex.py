fh=open('actual.txt')
import re
sum=0
for line in fh:
    str=re.findall('[0-9]+',line)
    for k in str:
        sum+=int(k)
print(sum)