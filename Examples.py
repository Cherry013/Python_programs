# import sys
#
# import os
#
# from functools import reduce

# Packages and modules
# 1. Write a Python program that attempts to dynamically import a module at runtime.
# The program should only import the module if it actually exists;
# otherwise, it should print "Module does not exist".
#
# n = input("Enter the module name: ")
# if n+".py" in os.listdir():
#     import importlib
#     n = importlib.import_module(n)
#     # k = input()
#     # importlib.reload(n)
# else:
#     print("File Not Found")
#
# without and with Error handling
#
# try:
#     n = input("Enter a module name: ")
#     import importlib
#     n = importlib.import_module(n)
# except Exception as e:
#     print(e)



# # 2nd Question
# 2. Create a Python package that contains two or more modules.
# Each module should define classes with attributes and methods.
# Then create another module outside the package, import the package modules,
# and create a subclass that inherits from at least one of the classes.
# Finally, create objects of both parent and child classes
#
# # D.py in subpack inside batch2 package
# class Animal:
#     def __init__(self, category):
#         self.category = category
#     def Wtype(self):
#         print(f"{self.category}")
#
# # C.py inside batch2 package
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def action(self):
#         print("Sleeping")
#
# # Q2.py outside batch2 pacage
# from batch2.C import Dog
# from batch2.subpack.D import *
#
# class pet(Dog):
#     def m1(self):
#         print(f"Name : {self.name}")
#
# k = pet("Broly")
# k.m1()
# k.action()
#
# an = Animal("Land animal")
# an.Wtype()


# # 3rd Question
# Create two Python modules that import each other. Run the program to observe what happens with circular imports.
# Then think of different ways to prevent a circular-import crash.
# # file1.py
# sel = 13
# li = [1,2,3,4]
# x = lambda n:(n*(n-1)/2)
#
# if __name__ == "__main__":
#     import file2
#
# if __name__ == "file1":
#     # import file1 # This will give ImportError
#     print(li)
#
# # file2.py
# a = 10
# B = 20
#
# if __name__ == "__main__":
#     import file1 as hell
#     print(hell.x(25))
#     print(hell.li)
#
#
# if __name__ == "file2":
#     # import file1 # This will give ImportError
#     print("Breaking circular importing")


# # 4th Question
# Create a package with a module containing an abstract base class (ABC).
# Another module in the same package should define concrete subclasses that implement all abstract methods.
# Write a driver program that imports these classes and demonstrates polymorphism.
#
# # Abclass.py inside batch2 package
# from abc import ABC, abstractmethod
#
# class Baseclass(ABC):
#     def __init__(self):
#         self.name = "baseclass"
#     @abstractmethod
#     def m1(self):
#         pass
#
# # CSubclass.py inside batch2 package
# from batch2.Abclass import Baseclass
#
# class Subclass(Baseclass):
#     """docstring for Subclass"""
#     def __init__(self,a):
#         super().__init__()
#         self.a = a
#
#     def m1(self):
#         print(f"Name : {self.name}")
#         print(f"running from {self.a}")
#
# class Subclass2(Baseclass):
#     def __init__(self):
#         super().__init__()
#         self.b = "Subclass2"
#
#     def m1(self):
#         print(f"{self.name} is running from {self.b}")
#
#
# if __name__ == "__main__":
#     obj = Subclass2()
#     obj1 = Subclass("Subclass1")
#     obj.m1()
#     obj1.m1()
#
#
# # Q4.py outside of the package
# from batch2.CSubclass import Subclass, Subclass2
#
# obj = Subclass("Subclass")
# obj.m1()
#
# obj1 = Subclass2()
# obj1.m1()
# print(type(obj1))
# print(Subclass.__dict__)
# print(Subclass2.mro())
#
# def fun(*obj):
#     for i in obj:
#         i.m1()
#
# fun(obj,obj1)


# 5. Create three modules:
# Module A: class Animal
# Module B: class Walkable
# Module C: class Dog that inherits from both Animal and Walkable
# Demonstrate method resolution order (MRO) by calling overridden methods and printing the MRO.
#
# # A.py
# class Animal:
#     def __init__(self, name, category):
#         super().__init__(category)
#         self.name = name
#     def Wtype(self):
#         print(f"{self.name}")
#         super().Wtype()
#
# # B.py
# class Walkable:
#     def __init__(self, category):
#         self.category = category
#     def Wtype(self):
#         print(f"{self.category}")
# # C.py
# import A,B
# class Dog(A.Animal,B.Walkable):
#     def __init__(self, name, Category):
#         super().__init__(name, Category)
#         super().Wtype()
#
# obj = Dog("Broly", "Land Animal")
# print(Dog.mro())
# print(Dog.__mro__)


# 6. Create a class in a module that uses private attributes and @property / @setter decorators.
# Import the class into another module and show how encapsulation protects the data while still allowing controlled access.
#
# # Demo.py
# import random
# class Demo:
#     def __init__(self, name):
#         self.name = name
#         self.__id = random.randint(1, 1000)
#
#     @property
#     def roll_num(self):
#         return self.__id
#     @roll_num.setter
#     def roll_num(self, roll_num):
#         x = input("Enter the pin : ")
#         if x == "123456":
#             self.__id = roll_num
#
#     def display(self):
#         print(f"Name : {self.name}\nRoll Number : {self.roll_num}")
#
# # testing.py
# from Demo import Demo
# st = Demo("Peter")
# st.display()
# st.roll_num = random.randint(1, 1000) # Enter wrong pin
# print(st.roll_num)
# st.roll_num = random.randint(1, 1000) # Enter Correct pin
# print(st.roll_num)


# 7. Create a module containing two classes where one uses composition and
# another uses inheritance to reuse code from a base class.
# Import and demonstrate the difference between the two approaches.
#
# # Mclass.py
# class Baseclass:
#     def display(self):
#         print("BaseClass")
#
# class inhertance(Baseclass):
#     def display(self):
#         super().display()
#         print("Using inhertance")
#
# class composition:
#     def display(self):
#         self.obj = Baseclass()
#         self.obj.display()
#         print("Using composition")
#
# # Dclass.py
# form Mclass import inhertance, composition
# x = inhertance()
# x.display()
# y = composition()
# y.display()
# y.obj.display()


# Map, Filter and reduce
# 1. Use map() with a lambda to add 5 to every element of the following nested
# list [[1, 2], [3, 4], [5, 6]]
#
# k = [[1, 2], [3, 4], [5, 6]]
# li = list(map(lambda x: [i+5 for i in x], k))
# print(li)

# 2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} .
# Use filter() to keep only the keys whose values are greater than 50.
#
# d = {"apple": 100, "banana": 40, "cherry": 150}
# l = dict(filter(lambda x: x[1] > 50, d.items()))
# print(l)

# 3. Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.
#
# from functools import reduce
# li = [int(input("Enter Number: ")) for _ in range(int(input("Enter list size: ")))]
# x = reduce(lambda x, y:x if x>y else y, li)
# print(x)

# 5. Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.
#
# st = input("Enter a text: ")
# li = list(map(ord, st))
# print(li)

# 6.  Use filter() to remove all vowels from a string and print the final string
# x = input("Enter a String: ")
# l = ['a','e','i','o','u','A','E','I','O','U']
# li = list(filter(lambda x:not x in l, x))
# print("".join(li))

#7.  Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n']
#
# from functools import reduce
# li = ['P', 'y', 't', 'h', 'o', 'n']
# li = reduce(lambda x,y: x+y, li)

# 8.  Given a list of integers, use map() with id() to print the memory address of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.
# l = [10, 350, 10, 350, 20]
# address = list(map(id,l))
# print(address)

# 10.  Given a list of numbers: [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers
#
# from functools import reduce
# l = [5, 10, 12, 20, 18, 26]
# li = reduce(lambda x,y: x+y,list(filter(lambda x: x%5==0,list(map(lambda x:x*x, l)))))
# print(li)

# # File Handling
#
# 1. Write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of characters in the file.
#
# Hello.txt file already created with some content
# with open("Hello.txt","r") as f:
#     l = f.read()
#     print(f.tell())
#     print(len(l))

# 2. Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10 characters.
#
# with open("hello.txt","r") as file:
#     li = file.readlines()
#     for i in li:
#         if len(i)>10:
#             print(i)

# 3. Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints the complete file content.
#
# with open("Hello.txt",'w') as f:
#     f.writelines(["Hii\n","Hello World\n","Who are you?"])
# with open("Hello.txt",'a') as f:
#     f.writelines(["\nUsing append writing lines\n","Just another line\n"])
# with open("Hello.txt",'r') as f:
#     print(f.read())

# 4. Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.
#
# with open("Hello.txt",'r') as f:
#     print(f"Up to first 10 index :{f.read(10)}")
#     f.seek(0)
#     print(f"Changed cursor position to {f.tell()}")
#     print(f" Complete content: {f.read()}")

# 5. Create a custom context manager using a class that opens a file in write mode
# in the __enter__ method, writes a line to the file, closes the file in the
# __exit__ method, and properly prints or logs any exception information received in __exit__.
#
# class WriteMode:
#     def __init__(self, fileName):
#         self.fileName = fileName
#
#     def __enter__(self):
#         self.f = open(self.fileName, 'w')
#         print("File opened in WriteMode")
#         return self.f
#     def __exit__(self, e_type, e_value, traceback):
#         print(f"type : {e_type}\n value : {e_value}\n traceback : {traceback}")
#         self.f.close()
#         print("File closed")
#
# with WriteMode("Hello.txt") as f:
#     f.write("Hello World")
#     print(f.read()) # Try this if you want exception


# 6. Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object, and ensures the file is closed
# even if an exception occurs.
#
# from contextlib import contextmanager
# @contextmanager
# def opening(FileName, mode="r"):
#     file = None
#     try:
#         file = open(FileName, mode)
#         yield file
#     except Exception as e:
#         print(e)
#     finally:
#         if file is not None:
#             file.close()
#
# with opening("Hello.txt") as file:
#     print(file.read())
#     print(f"Closed? {file.closed}")
# print(f"Closed? {file.closed}")


# 7. Write a program using a context manager that opens a file in read mode, uses a
# loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(), uses seek() to move to
# a specific position, and continues reading from there.
#
# with open("Hello.txt", 'r') as f:
#     while True:
#         chunk = f.read(10)
#         print(f"Chunk: {chunk}  Cursor position: {f.tell()}")
#         if not chunk: # or chunk == ""
#             break
#     cur = int(input("Enter cursor position: "))
#     f.seek(cur)
#     print(f"Cursor Position: {f.tell()}")
#     print(f.read())


# for i in range(456):
#     print(f"HexValue({i}): {hex(i)}")