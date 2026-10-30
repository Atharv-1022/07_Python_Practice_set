'''Write a program that asks the user to enter a number and handles:

ValueError if the input is not a number
ZeroDivisionError if you try to divide by zero'''

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

try:
    Ans=num1/num2
except ValueError:
    print("Plz Do not  perform different typecasting ")
except ZeroDivisionError:
    print("Plz do not try to divid by zero")
except Exception as e:
    print("Unknow error",e)

