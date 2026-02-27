# 1: Простое наследование
class Animal:
    def speak(self): print("Some sound")
class Dog(Animal): pass
Dog().speak()

# 2: Наследование с __init__
class Person:
    def __init__(self,name): self.name=name
class Student(Person): pass
print(Student("Aruzhan").name)

# 3: Переопределение метода
class Dog(Animal):
    def speak(self): print("Woof!")
Dog().speak()

# 4: Добавление метода в потомке
class Cat(Animal):
    def meow(self): print("Meow!")
c=Cat(); c.speak(); c.meow()