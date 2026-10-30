#Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].
from functools import reduce
numbers=[1, 2, 3, 4]

def product(x,y):
    return x*y

num=reduce(product,numbers)

print(num)