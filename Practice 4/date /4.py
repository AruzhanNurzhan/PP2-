#Write a Python program to calculate two date difference in seconds.
import datetime
a=datetime.datetime(2026,2,27,12,0,0)
b=datetime.datetime(2025,3,23,16,4,5)
c=a-b
d=c.total_seconds()
print(d)

