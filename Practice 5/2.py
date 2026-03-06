#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
n=input()
pattern=r"ab{2,3}"
m=re.findall(pattern,n)
print(m)