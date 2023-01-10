# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg=0 
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(' ')
    pis=line.find('\n')
    avg=avg+float(line[pos+1:pis])
    count+=1
print('Average spam confidence:',float(avg/count))