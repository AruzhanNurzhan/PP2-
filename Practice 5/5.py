#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
n=input()
pattern=r"a.*b$"
m=re.findall(pattern,n)
print(m)