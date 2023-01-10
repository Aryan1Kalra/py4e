name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
counts=dict()
handle = open(name)
for line in handle:
    if('From ' in line):
        words=line.split()
        word=words[1]
        counts[word]=counts.get(word,0)+1
mcount=None
mail=None
for k,v in counts.items():
    if mcount is None or mcount<v:
        mcount=v
        mail=k
print(mail,mcount)