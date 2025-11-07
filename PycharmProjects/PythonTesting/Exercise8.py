with open("file1.txt","r") as f:
    count=0
    for line in f.readlines():
        print(line)
        count=count+1
        print("The total number of lines is ",count)