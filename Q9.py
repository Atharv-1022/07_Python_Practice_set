#Use filter() to get only even numbers from [10, 11, 12, 13, 14].
numbers=[10, 11, 12, 13, 14]

def even_numbers(x):
    if x%2==0:
        return True
    else:
        return False

num=list(filter(even_numbers,numbers))
print(num)
