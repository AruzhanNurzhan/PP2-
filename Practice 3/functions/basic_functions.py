# 1: Функция без аргументов, просто печатает текст
def greet():
    print("Hello, world!")
greet()

# 2: Функция с аргументом, выводит имя
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Aruzhan")

# 3: Функция с двумя аргументами, складывает числа
def add(a, b):
    print(a+b)
add(5,7)

# 4: Функция с return, возвращает произведение
def multiply(a, b):
    return a*b
print(multiply(3,4))