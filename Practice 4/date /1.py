#Write a Python program to subtract five days from current date.
import datetime
a=datetime.datetime.now()
b=a-datetime.timedelta(days=5)
print(b)