
# To create and Write a sentences in the file or if the file exists it write in it from the start
# f = open("Demo.txt","w")
# f.write("Hello, This is Charan I am writing in a new file")
# f.close()

# Another Ways to write, this way You don't need to close it closes automatically
# with open("Demo.txt","w") as file:
#     file.write("I am using Python Programming \nNothing Just using new line \nJust using it")

#
# with open("Demo.txt","r") as file:
#     print(file.read())

# To read the existing txt file
# f = open("Demo.txt","r")
#
# print(next(f))
# print(next(f))
# print(next(f))
# print(f)
#
# d = f.read()
# print(type(d))
# print(d)
#
# print(f.readline()) # It Reads only one line
# print(f.readlines()) # It reads all lines


# append new lines to the existing file
# with open("Demo.txt","a") as file:
#     file.write("\nI am appending to the Current txt file")

# using binary
# with open("Demo.txt","rb") as file:
#     print(file)
#     data = file.read()
#     print(data)
# with open("demo.txt","wb") as file:
#     file.write(data)

# About Cursor Positions
# with open("Demo.txt","r") as file:
#     print(file.tell()) # Tells the Cursor position
#     print(file.read(50)) # Reads the file upto 25th position
#     print(file.tell()) # Shows 26 because 25 completed reading
#     print(file.seek(30)) # Sets the Cursor position
#     print(file.tell())  # Shows the position Curser was set
#     print(file.read()) # Starts reading from the Position set for Cursor
#

# about 'os' Function
# import os
# print(os.getcwd())
# print(os.getpid())
# print(os.path.exists("Demo.txt")) # Can be used to check weather the file exists or not
# # os.remove("Demo.txt") # can be used to remove or delete the file
# os.rename("Demo.txt", "Printing.txt") # can be used to rename the file
