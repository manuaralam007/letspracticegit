# How to write a full_name_with_age through code

def get_full_name_with_age(first_name:str, last_name:str, age:str):
    name_with_age = first_name.capitalize() + " " + last_name.capitalize() + " is " + str(age) + " years old"
    return name_with_age

print(get_full_name_with_age("manuar", "alam", "27"))
