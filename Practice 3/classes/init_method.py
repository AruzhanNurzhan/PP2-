# 1: __init__ с одним аргументом
class Person:
    def __init__(self,name): self.name=name
print(Person("Aruzhan").name)

# 2: __init__ с двумя аргументами
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
s=Student("Dana","A")
print(s.name,s.grade)

# 3: __init__ с листом
class Team:
    def __init__(self,members): self.members=members
print(Team(["Aruzhan","Dana"]).members)

# 4: Изменение свойства объекта
class Car:
    def __init__(self,model): self.model=model
c=Car("Tesla")
c.model="BMW"
print(c.model)