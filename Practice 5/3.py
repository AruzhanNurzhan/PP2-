#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
n=input()
pattern=r"[a-z]*_"
m=re.findall(pattern,n)
print(m)