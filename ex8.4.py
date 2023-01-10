fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    x=line.split()
    print(x)
    for i in range(len(x)):
        if(x[i] not in lst):
            lst.append(x[i])
lst.sort()
print(lst)