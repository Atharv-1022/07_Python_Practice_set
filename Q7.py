#Create a custom exception NegativeNumberError and raise it when the user enters a negative number.
class NegativeNumberError(Exception):
    pass

num=int(input("Enter a number:"))
try:
    if num<0:
        raise NegativeNumberError("The number cant put Negative number")
    result=45/num

    print(f"Result is {result}")
except ValueError:
    print("Plz Dont perform typecasting")

except ZeroDivisionError:
    print("plz Dont divide by zero")
except NegativeNumberError as e:
    print(f"Error {e}")