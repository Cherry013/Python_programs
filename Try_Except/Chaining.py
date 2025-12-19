
# Error Chaining
# try:
#     a = int(input("Enter a number: ")) # TypeError may occur
#     b = int(input("Enter another number: "))
#     try:
#         c = a/b # ZeroDivision Error may occur
#     except Exception as e:
#         print(e)
# except Exception as e:
#     print(e)
# # else:
# #     print(c)

# try:
#     x = int(input("Enter a number: "))
#     assert x>0, "Number Should be Positive"
#     print(x)
# except Exception as e:
#     print(e)

# try:
#     a = input("Enter Something: ")
# except EOFError:
#     print("EOFError")

# try:
#     a = int(input())
#     if a > 0:
#         raise ValueError()
#         print("Hello")
# except Exception as e:
#     print(e,e.__class__)
# else:
#     print(a)
# finally:
#     print("Completed")