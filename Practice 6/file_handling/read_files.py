
#read entire file
with open("data.txt", "r") as f:
    # read() returns the file content
    print(f.read())
#read one line
with open("data.txt","r") as f:
    # readline() returns one line from the file
    print(f.readline())
#read all lines as list
with open ("data.txt","r") as f:
    #readlines() returns a list of lines from the file
    print(f.readlines())
