#  1: 
class Dog:
    def bark(self):
        print("Woof!")
my_dog = Dog()
my_dog.bark()

#  2: 
class Cat:
    def meow(self):
        print("Meow!")
    def sleep(self):
        print("Zzz...")
my_cat = Cat()
my_cat.meow()
my_cat.sleep()

#  3: 
class Person:
    def introduce(self, name):
        print(f"My name is {name}")
p = Person()
p.introduce("Aruzhan")

#  4:
class Calculator:
    def multiply(self, a, b):
        print(a * b)
calc = Calculator()
calc.multiply(5, 6)