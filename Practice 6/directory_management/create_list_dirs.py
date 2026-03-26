import os

# Create nested directories
nested_path = "dir1/dir2/dir3"
if not os.path.exists(nested_path):
    os.makedirs(nested_path)

# List files and folders in current directory
for item in os.listdir():
    print(item)

# Find files by extension (.txt)
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)