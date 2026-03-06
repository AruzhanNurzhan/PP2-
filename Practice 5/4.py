#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
n=input()
pattern=r"[A-Z][a-z]+"
m=re.findall(pattern,n)
print(m)