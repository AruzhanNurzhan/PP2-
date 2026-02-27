students=[('Aruzhan',95),('Bek',88),('Dana',92)]

# 1: Сортировка по оценке по убыванию
print(sorted(students,key=lambda s:s[1],reverse=True))

# 2: Сортировка по имени
print(sorted(students,key=lambda s:s[0]))

# 3: Сортировка по первой букве имени
print(sorted(students,key=lambda s:s[0][0]))

# 4: Сортировка по остатку от деления оценки на 10
print(sorted(students,key=lambda s:s[1]%10))