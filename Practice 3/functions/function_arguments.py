# 1
def describe_pet(name, animal_type):
    print(f"{animal_type} named {name}")
describe_pet("Whiskers","cat")

# 2
def describe_pet_default(name, animal_type="dog"):
    print(f"{animal_type} named {name}")
describe_pet_default("Buddy")

# 3
def sum_numbers(*numbers):
    print(sum(numbers))
sum_numbers(1,2,3,4)

# 4
def build_profile(first,last,**info):
    profile = {'first': first, 'last': last}
    profile.update(info)
    print(profile)
build_profile("Aruzhan","Nurzhan", location="Almaty", field="Physics")