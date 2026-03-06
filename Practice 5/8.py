#Write a Python program to split a string at uppercase letters.
import re
n=input()
pattern=r"(?=[A-Z])"
m=re.split(pattern,n)
print(m)