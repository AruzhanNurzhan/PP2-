#Write a Python program to drop microseconds from datetime
import datetime
b=datetime.datetime.now().replace(microsecond=0)
print(b)