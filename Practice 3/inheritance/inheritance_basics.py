# 1
class Animal:
    def speak(self): print("Some sound")
class Dog(Animal): pass
Dog().speak()

# 2
class Person:
    def __init__(self,name): self.name=name
class Student(Person): pass
print(Student("Aruzhan").name)

# 3
class Dog(Animal):
    def speak(self): print("Woof!")
Dog().speak()

# 4
class Cat(Animal):
    def meow(self): print("Meow!")
c=Cat(); c.speak(); c.meow()