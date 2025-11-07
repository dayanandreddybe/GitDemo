try:
    with open("file3.txt","r")as reader:
        for line in reader.readlines():
            print(line)
except Exception as e:
    print(e)
    print("Some how i entered this block")
finally:
    print("Cleaning up the resources")