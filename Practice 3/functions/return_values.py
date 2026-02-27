# 1: Возврат одного значения
def square(x):
    return x**2
print(square(5))

# 2: Возврат нескольких значений
def powers(x):
    return x**2, x**3
print(powers(3))

# 3: Возврат True/False
def is_even(n):
    return n%2==0
print(is_even(4))

# 4: Возврат списка
def even_numbers_list(n):
    return [x for x in range(n) if x%2==0]
print(even_numbers_list(10))