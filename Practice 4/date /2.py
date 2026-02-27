#Write a Python program to print yesterday, today, tomorrow.

import datetime
a=datetime.datetime.now()
b=a-datetime.timedelta(days=1)
c=a+datetime.timedelta(days=1)
print(b)
print(a)
print(c)