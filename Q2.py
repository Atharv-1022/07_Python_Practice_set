'''Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.'''

from time import time
def timer (func):
    def wrapper(n):
        t1=time()
        func
        t2=time()
        print(t2-t1)
    return wrapper

@timer
def sum(n):
    sum1=0
    for i in range(1,n+1):
        sum1+=i
    return sum1

a=sum(100000000)
