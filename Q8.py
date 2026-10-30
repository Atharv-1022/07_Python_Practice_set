#Use map() to convert [1, 2, 3, 4, 5] into their cubes.
numbers=[1, 2, 3, 4, 5]
def cubes(n):
    return n**3
num=list(map(cubes,numbers))
# num=list(map(lambda x:x*3,numbers))

print(num)
