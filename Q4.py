'''Create a class MathUtils with:

A @staticmethod called add(a, b) that returns a + b.
A @classmethod called description(cls) that prints "This is a utility class for math operations."'''

class MathUtils:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def descripstion(cls):
        print("This is a utility class for math operations.")

M=MathUtils("Atharv",12313)

print(M.add(112,23))
M.descripstion()

#Call both methods without creating an object.
print(MathUtils.add(2,3))
MathUtils.descripstion()

