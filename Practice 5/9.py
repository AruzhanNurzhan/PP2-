#Write a Python program to insert spaces between words starting with capital letters.
import re
n=input()
pattern = r"(?<!^)([A-Z])"
m = re.sub(pattern, r" \1", n)
print(m)