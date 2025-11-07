with open("test2.txt","w")as writer:
    writer.writelines("Hi ,HElo ,How r u")

with open("test2.txt","r")as reader:
    for line in reader.readlines():
        print(line)