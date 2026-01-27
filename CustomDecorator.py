# Demo
import functools
def Decorator(func):
    def wrapper(x, y):
        print("Decorator Heading")
        x = func(x,y)
        x+=(x*x)
        print("Decorator Footer")
        return x

    return wrapper

@Decorator
def fun(x,y):
    return x+y

print(fun(2,3))
print(Decorator().__dict__)