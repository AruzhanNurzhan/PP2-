numbers=[1,2,3,4,5]

# 1
print(list(map(lambda x:x**2,numbers)))

# 2
print(list(map(lambda x:x+10,numbers)))

# 3
print(list(map(lambda x:f"Number {x}",numbers)))

# 4
print(list(map(lambda x:x%2==0,numbers)))