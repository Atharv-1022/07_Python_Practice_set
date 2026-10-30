# Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Funcstion stared...")
        result=func(*args, **kwargs)
        print("Funcstion fineshed...")
        return result()
    return wrapper()
@decorator
def add(a,b):
    return a+b
@decorator
def print_info(name,age):
    return f'Hi {name}, my age is {age}'

print(add(9,8))

print(print_info("Atharv",22))