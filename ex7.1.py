# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
str=fh.read()
str=str.upper()
str=str.rstrip()
print(str)