# 1: *args для суммы чисел
def sum_all(*args):
    print(sum(args))
sum_all(1,2,3,4,5)

# 2: **kwargs для характеристик
def print_user(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")
print_user(name="Aruzhan", age=20, city="Almaty")

# 3: Комбинация обычных аргументов + *args
def greet_people(greeting,*names):
    for n in names:
        print(f"{greeting}, {n}!")
greet_people("Hello","Aruzhan","Dana")

# 4: Комбинация обычных аргументов + **kwargs
def describe_person(name,**attributes):
    print(f"Person: {name}")
    for k,v in attributes.items():
        print(f"{k}: {v}")
describe_person("Aruzhan", age=20, field="Physics")