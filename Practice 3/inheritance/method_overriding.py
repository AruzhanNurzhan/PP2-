# 1: Родительский метод
class Animal:
    def speak(self): print("Some sound")

# 2: Переопределение метода
class Dog(Animal):
    def speak(self): print("Woof!")
Dog().speak()

# 3: Переопределение + вызов родителя
class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow!")
Cat().speak()

# 4: Полное переопределение
class Bird(Animal):
    def speak(self): print("Tweet!")
Bird().speak()