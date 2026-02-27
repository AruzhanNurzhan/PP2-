# 1: Переменная класса
class Student: school="NIS"
s1=Student(); s2=Student()
print(s1.school,s2.school)

# 2: Переменная экземпляра
s1.name="Aruzhan"; s2.name="Dana"
print(s1.name,s2.name)

# 3: Изменение переменной класса
Student.school="New School"
print(s1.school,s2.school)

# 4: Удаление свойства объекта
del s1.name
# print(s1.name) # вызовет ошибку