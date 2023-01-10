fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
lst=list()
fh = open(fname)
count = 0
for line in fh:
    if(line.startswith('From')):
        if('From:' not in line):
            lst=line.split()
            print(lst[1])
            count+=1

print("There were", count, "lines in the file with From as the first word")
