# Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.

class Vector:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def __add__(self,num):
        return Vector(self.num1+num.num1 ,self.num2+num.num2)

    def print_info(self):
        print(f"{self.num1},{self.num2}")


v1=Vector(2,3)
v2=Vector(3,4)

v3=v1+v2

v3.print_info()