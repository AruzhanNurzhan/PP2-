# 1
class Animal:
    def speak(self): print("Some sound")

# 2
class Dog(Animal):
    def speak(self): print("Woof!")
Dog().speak()

# 3
class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow!")
Cat().speak()

# 4
class Bird(Animal):
    def speak(self): print("Tweet!")
Bird().speak()