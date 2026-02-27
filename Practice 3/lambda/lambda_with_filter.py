numbers=[10,15,20,25,30]

# 1
print(list(filter(lambda x:x%2==0,numbers)))

# 2
print(list(filter(lambda x:x>20,numbers)))

# 3
print(list(filter(lambda x:x<25,numbers)))

# 4
print(list(filter(lambda x:x%5==0,numbers)))