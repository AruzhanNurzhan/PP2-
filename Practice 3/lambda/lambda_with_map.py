numbers=[1,2,3,4,5]

# 1: Квадраты элементов
print(list(map(lambda x:x**2,numbers)))

# 2: Увеличение на 10
print(list(map(lambda x:x+10,numbers)))

# 3: Преобразование в строки
print(list(map(lambda x:f"Number {x}",numbers)))

# 4: Проверка на чётность
print(list(map(lambda x:x%2==0,numbers)))