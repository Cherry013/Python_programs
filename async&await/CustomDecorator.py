# Demo
import functools
import time


def Decorator(func):
    def wrapper(x, y):
        print("Decorator Heading")
        z = func(x, y)
        z+=(z * z)
        print(f"X: {x} & Y: {y} calculation of (X+Y+(X+Y)**2) : {z}")
        print("Decorator Footer")
        return z

    return wrapper

@Decorator
def fun(x,y):
    return x+y

# fun(2,3)
# print(Decorator.__dict__)


# Looping using decorators
def rep(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@rep(2)
def Hello(a,b):
    """Hello This is Document String"""
    print(f"Hello World {a} & {b}")

# Hello(1,2)
# print(Hello.__doc__)

# Validations using Custom decorators
def validations(fun):
    @functools.wraps(fun)
    def wrapper(x,y):
        if x < 0 or y < 0:
            raise ValueError("x and y must be non-negative")
        return fun(x,y)
    return wrapper

@validations
def distance(x,y):
    return (x**2) + (y**2)

# print(distance(0    ,2))
# print(distance(1,-2))


# Timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # start = time.asctime()
        start = time.time()
        print("Started: ", start)
        print(func(*args, **kwargs))
        # end = time.asctime().split()
        end = time.time()
        print("Time taken: ",end-start)
    return wrapper

@timer
def add(x,y):
    su = 0
    for i in range(1, x + y + 1):
        su += i
    return su

# add(10,20)
# print(time.asctime())
# print(list(time.asctime().split()))

def dec(fn):
    @functools.wraps(fn)
    def indec(*args, **kwargs):
        print("Just adding 2sec Delay to start the function")
        time.sleep(2)
        result = fn(*args,**kwargs)
        print("Execution Completed")
        print()
        return result
    return indec

@dec
def add(a,b,c):
    """ Just adding A DOC"""
    return a+b+c

# print(add.__doc__)
# print(add(1,2,3))


def tim(delay):
    def dec(fn):
        @functools.wraps(fn)
        def indec(*args, **kwargs):
            print(f"Just adding {delay}sec Delay to start the function")
            print(f"Address inside Decorator : {fn}")
            time.sleep(delay)
            result = fn(*args,**kwargs)
            print("Execution Completed")
            print()
            return result
        print(f"Address indec : {indec}")
        return indec
    return dec

k = int(input("Enter Delay : "))
@tim(k)
def add(a,b,c):
    """ Just adding A DOC"""
    return a+b+c
print(f"Address add : {add}")
print(add(10,15,25))