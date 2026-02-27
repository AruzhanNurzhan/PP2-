# 1: Позиционные аргументы
def describe_pet(name, animal_type):
    print(f"{animal_type} named {name}")
describe_pet("Whiskers","cat")

# 2: Аргумент по умолчанию
def describe_pet_default(name, animal_type="dog"):
    print(f"{animal_type} named {name}")
describe_pet_default("Buddy")

# 3: *args - произвольное количество аргументов
def sum_numbers(*numbers):
    print(sum(numbers))
sum_numbers(1,2,3,4)

# 4: **kwargs - произвольные именованные аргументы
def build_profile(first,last,**info):
    profile = {'first': first, 'last': last}
    profile.update(info)
    print(profile)
build_profile("Aruzhan","Nurzhan", location="Almaty", field="Physics")