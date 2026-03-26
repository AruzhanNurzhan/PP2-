import shutil
import os

# Move data.txt to dir1
if os.path.exists("data.txt"):
    shutil.move("data.txt", "dir1/data.txt")

# Copy file back to current directory
if os.path.exists("dir1/data.txt"):
    shutil.copy("dir1/data.txt", "data_copy.txt")