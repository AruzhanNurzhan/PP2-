#Write a Python program to convert a given camel case string to snake case.
import re
n=input()
m=re.sub(r'(?<!^)([A-Z])', r'_\1', n)
m=m.lower()
print(m)