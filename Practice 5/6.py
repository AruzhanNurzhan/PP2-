#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re 
n=input()
pattern=r"[ ,.]"
m=re.sub(pattern,":",n)
print(m)