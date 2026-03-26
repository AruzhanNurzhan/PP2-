import shutil
import os

# shutil.copy() copies file
shutil.copy("data.txt", "backup.txt")

# Check if file exists before deleting
if os.path.exists("backup.txt"):
    # os.remove() deletes file
    os.remove("backup.txt")
    