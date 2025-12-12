# 1.
# try:
#     age = int(input("Enter you age: "))
#     if age > 18:
#         print("Pass")
#     else:
#         print("Fail")
#
# except Exception as e:
#     print(f"You've entered Invalid Integer with exception ==>({e}) , you need to enter numbers like --> 12,15,18etc..")
#     age = int(input("Enter your age: "))
#     if age > 18:
#         print("Pass")
#     else:
#         print("Fail")
#
# else:
#     print("done")
#
# finally:
#     print("Completed")

# Raise Error -- ValueError
# def Square(x):
#     if x<0:
#         raise ValueError("X should not be negative")
#     return x*x
#
# print(Square(25))
# print(Square(-25))


# TypeError
# def add(x,y):
#     if not (isinstance(x, int) and isinstance(y, int)):
#         raise TypeError("Both arguments must be integers")
#     return x+y
#
# print(add(25,33))
# print(add("hello",33))


# Re-raising error
# try:
#     10/0
# except ZeroDivisionError:
#     print("Error resolved but re-raising here")
#     raise ZeroDivisionError("10/0 Not possible")


# Custom error -- 1
# class OTPError(Exception):
#     pass
#
# try:
#     def OTP(otp):
#         ver = 123654
#         if ver != otp:
#             raise OTPError("Wrong OTP Entered")
#         return True
#
#     print(OTP(12364))
#     print(OTP(123654))
#
# except OTPError:
#     print("OTP Error Raised")
#
# else:
#     print("Error not raised")
#
# finally:
#     print("Action Completed")


# Custom error -- 2
#
# class AgeError(Exception):
#     def __init__(self, age, msg):
#         self.age = age
#         self.message = msg
#         super().__init__(f" {self.message} \n Given Age : {self.age}")
#
# try:
#     a = int(input())
#     if a<0:
#         raise AgeError(a, "Age should be greater than 0")
#
# except AgeError:
#     print("Age is in negative")
# except Exception as e:
#     print(f"Error ==>  {e}")
#
# else:
#     print("Age is ok")
#
# finally:
#     pass


# Exception Hierarchy
# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  └── Exception
#       ├── ArithmeticError
#       │     ├── ZeroDivisionError
#       │     └── OverflowError
#       ├── LookupError
#       │     ├── IndexError
#       │     └── KeyError
#       ├── ValueError
#       ├── TypeError
#       ├── FileNotFoundError
#       └── RuntimeError

# Examples of Hierarchy
# try:
#     x=10/0
#     x = [1,2,3]
#     print(x[10])
# except LookupError as e:
#     print(e)
#     print("It should be an IndexError but IndexError is a child of Parent class it will get caught")
# except ZeroDivisionError as e:
#     print(e)
#     print("ZeroDivisionError is different this is how hierarchy works")

# about logging
# import logging
#
# try:
#     10/0
# except ZeroDivisionError as e:
#     # logging.log(1,"Error occurred \n %s",e)
#     logging.error("Error occurred \n %s",e)
    # logging.warning("Error occurred \n %s",e)