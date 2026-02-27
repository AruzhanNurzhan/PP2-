# 1
class Person:
    def __init__(self,name): self.name=name
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
s=Student("Aruzhan","A")
print(s.name,s.grade)

# 2
class Animal:
    def speak(self): print("Some sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")
Dog().speak()

# 3
class Employee(Person):
    def __init__(self,name,position):
        super().__init__(name)
        self.position=position
print(Employee("Dana","Manager").name)

# 4
class Base:
    def greet(self): print("Hello from Base")
class Derived(Base):
    def greet(self):
        super().greet()
        print("Hello from Derived")
Derived().greet()