# 1
def square(x):
    return x**2
print(square(5))

# 2
def powers(x):
    return x**2, x**3
print(powers(3))

# 3
def is_even(n):
    return n%2==0
print(is_even(4))

# 4
def even_numbers_list(n):
    return [x for x in range(n) if x%2==0]
print(even_numbers_list(10))