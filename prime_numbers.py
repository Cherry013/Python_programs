class Prime:
    def __init__(self,num):
        self.num = num

    def Check(self):
        if(self.num <= 1):
            return -1
        else:
            flag = 0
            for i in range(2,int(self.num/2)+1):
                if(self.num%i == 0):
                    flag = 1
            if(flag == 0):
                return 1
            else:
                return 0

prime = Prime(7)
print(prime.Check())

def add(n1,n2):
    return n1 + n2
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def division(a,b):
    return a//b
def mod(a,b):
    return a%b

oper = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division,
    "%":mod
}

a = int(input("Enter 'a' number: "))
b = int(input("Enter 'b' number: "))
op = input("Enter the operation u like from these '+, -, *, /, %' : ")
ans = oper[op](a,b)
print(ans)