file=open("test.txt")
#for line in file:
#    print(line)
for line in file.readlines():
    print(line)
    print(type(line))