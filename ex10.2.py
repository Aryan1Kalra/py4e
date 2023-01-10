name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
count=dict()
lst=list()
for line in fh:
    if('From ' in line):
        words=line.split()
        time=words[5]
        hr=time[0:2]
        count[hr]=count.get(hr,0)+1
#print(sorted([(k,v) for k,v in count.items()]))
for k,v in count.items():
    newtup=(k,v)
    lst.append(newtup)
lst=sorted(lst)
for k,v in lst:
    print(k,v)