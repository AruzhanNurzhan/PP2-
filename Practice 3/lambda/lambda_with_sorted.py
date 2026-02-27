students=[('Aruzhan',95),('Bek',88),('Dana',92)]

# 1
print(sorted(students,key=lambda s:s[1],reverse=True))

# 2
print(sorted(students,key=lambda s:s[0]))

# 3
print(sorted(students,key=lambda s:s[0][0]))

# 4
print(sorted(students,key=lambda s:s[1]%10))