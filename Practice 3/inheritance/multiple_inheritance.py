# 1
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

Child().skills()  # вызовет метод Father, так как первый родитель