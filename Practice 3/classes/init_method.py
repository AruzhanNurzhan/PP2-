# 1
class Person:
    def __init__(self,name): self.name=name
print(Person("Aruzhan").name)

# 2
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
print(Student("Dana","A").name, Student("Dana","A").grade)

# 3
class Team:
    def __init__(self,members): self.members=members
print(Team(["Aruzhan","Dana"]).members)

# 4
class Car:
    def __init__(self,model): self.model=model
c=Car("Tesla")
c.model="BMW"
print(c.model)