# 1: Метод без параметров
class Circle:
    def area(self): print("Area method called")
Circle().area()

# 2: Метод с self, вычисление площади
class Circle:
    def __init__(self,radius): self.radius=radius
    def area(self): return 3.14*self.radius**2
print(Circle(5).area())

# 3: Метод для изменения свойства
class Circle:
    def __init__(self,radius): self.radius=radius
    def change_radius(self,new_radius): self.radius=new_radius
c=Circle(5)
c.change_radius(10)
print(c.radius)

# 4: Метод возвращает строку
class Circle:
    def __init__(self,radius): self.radius=radius
    def describe(self): return f"Circle with radius {self.radius}"
print(Circle(10).describe())