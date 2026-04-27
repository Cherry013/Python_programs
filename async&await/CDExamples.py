def Dec(func):
    def Inner(*a,**b):
        print("Starting...")
        print(a,b,sep="\n")
        func(*a,**b)
        print("Done")
    # print(f"Inner : {Inner}")
    # print(f"func : {func}")
    return Inner

# @Dec
# def greet(s):
#     print(f"Hello {s}")
# # print(f"Greet : {greet}")
# greet("Ravi")

def multiplyer(func):
    def Inner(*a,**b):
        print("Starting...")
        print(a,b,sep="\n")
        x = func(*a,**b)
        x *=2
        return x
    return Inner

@multiplyer
def adding(x,y):
    return x+y

# print(adding(x=2,y=3))
# print(adding(3,4))

def access(func):
    def Inner():
        a = input("Enter your role : ")
        if a.lower() == "student":
            print("access denied")
        elif a.lower() == "admin":
            func()
        else:
            print("Invalid User")

    return Inner

@access
def user():
    print("Secured File")
#
# user()

def uppercase(func):
    def Inner(*a,**b):
        y = func(*a,**b)
        return y.upper()
    return Inner

@uppercase
def st(x):
    return x.lower()

# print(st("Hello World"))

def callCounter(func):
    c = 0
    def Inner(*a,**b):
        func(*a,**b)
        nonlocal c
        c+=1
        print(f"Counter : {c}")
    print(f"func : {func}")
    print(f"Inner : {Inner}")
    return Inner


# @callCounter
def counting():
    print("Counting")

print(f"Before counting : {counting}")
counting = callCounter(counting)
print(f"After counting : {counting}")

















