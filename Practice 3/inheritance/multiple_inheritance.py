# 1: Наследование от двух родителей
class Father:
    def skills(self): print("Gardening")
class Mother:
    def skills(self): print("Cooking")
class Child(Father,Mother): pass
Child().skills()

# 2: Добавление метода в потомке
class Child(Father,Mother):
    def play(self): print("Playing football")
Child().play()

# 3: Переопределение метода
class Child(Father,Mother):
    def skills(self): print("Coding")
Child().skills()

# 4: Вызов метода родителя + свой код
class Child(Father,Mother):
    def skills(self):
        super().skills()
        print("Painting")
Child().skills()