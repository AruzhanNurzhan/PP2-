# Open file in write mode (overwrites file if it exists)
with open("data.txt", "w") as f:
    f.write("Hello\n")          
    f.write("This is Python\n") 
    f.write("File handling\n") 
#Create a new file called "myfile.txt":
f = open("myfile.txt", "x")
#append to the end of the file
with open("data.txt","a") as f:
    f.write("Now the file has more content")
