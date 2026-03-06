#Write a python program to convert snake case string to camel case string.
import re
n = input()
m = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), n)
print(m)