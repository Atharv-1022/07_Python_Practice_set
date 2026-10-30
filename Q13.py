#Write a function sum_all(*args) that accepts any number of integers and returns their sum

def sum_all(*args):
    Total=0
    for item in args:
        Total+=item
    return Total

print(sum_all(1,2,3,4,5,6))