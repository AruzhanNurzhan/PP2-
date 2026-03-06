#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
n="a,abbd,abb,xge,abbbbbb,ab"
pattern=r"ab*"
m=re.findall(pattern,n)
print(m)