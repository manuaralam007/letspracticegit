# How to write a full_name through code

def get_full_name_with_age(name:str, age:str):
    name_with_age = name.capitalize() + " is " + str(age) + " years old"
    return name_with_age

print(get_full_name_with_age("manuar","27"))
