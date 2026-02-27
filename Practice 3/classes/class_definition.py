# 1: Простой класс с методом
class Dog:
    def bark(self):
        print("Woof!")
Dog().bark()

# 2: Класс с двумя методами
class Cat:
    def meow(self): print("Meow!")
    def sleep(self): print("Zzz...")
c=Cat()
c.meow()
c.sleep()

# 3: Метод с self
class Person:
    def introduce(self,name): print(f"My name is {name}")
Person().introduce("Aruzhan")

# 4: Метод с параметрами
class Calculator:
    def multiply(self,a,b): print(a*b)
Calculator().multiply(5,6)