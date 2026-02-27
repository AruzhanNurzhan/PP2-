# 1: Простая лямбда x**2
square = lambda x: x**2
print(square(5))

# 2: Лямбда с двумя аргументами
add = lambda a,b: a+b
print(add(3,4))

# 3: Лямбда для проверки четности
is_even = lambda x: x%2==0
print(is_even(6))

# 4: Лямбда с тернарным оператором (максимум)
max_value = lambda a,b: a if a>b else b
print(max_value(10,20))