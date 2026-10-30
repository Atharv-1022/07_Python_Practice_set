# Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing.
class log_error(Exception):
    pass

try:
    text=input("Enter your name:")
    password=int(input("Enter your pass:"))

    if text !="Atharv" and password!=123456:
        raise log_error("log Error ,plz cheak if the name or pass is right")
    print("Login Sucessfully,Welcome user!")
except log_error as e:
    print(e)