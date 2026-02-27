numbers=[10,15,20,25,30]

# 1: Чётные числа
print(list(filter(lambda x:x%2==0,numbers)))

# 2: Числа >20
print(list(filter(lambda x:x>20,numbers)))

# 3: Числа <25
print(list(filter(lambda x:x<25,numbers)))

# 4: Кратные 5
print(list(filter(lambda x:x%5==0,numbers)))